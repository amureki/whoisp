import logging
import re
from importlib import import_module

logger = logging.getLogger(__name__)


class MainParser:
    attributes_regex = {
        'creation_date': 'Creation Date: *(.+)',
        'domain_name': 'Domain Name: *(.+)',
        'expiration_date': 'Expir\w+ Date: *(.+)',
        'name_servers': 'Name Server: *(.+)',
        'org': 'Registrant\s*Organization: *(.+)',
        'registrar': 'Registrar: *(.+)',
        'status': 'Status: *(.+)',
    }

    def __init__(self, raw_whois):
        self.parsed = {}
        self.raw = raw_whois
        self.parse()

    def parse(self):
        for attribute, regex in self.attributes_regex.items():
            data = re.findall(regex, self.raw, re.IGNORECASE)
            self.parsed[attribute] = data
        return self.parsed

    @staticmethod
    def load(domain, raw_whois):
        domain_zone = domain.rsplit('.', 1)[1]
        parser_class_name = '{}Parser'.format(domain_zone.capitalize())
        parser_module = import_module('whoisp.parser')
        try:
            parser = getattr(parser_module, parser_class_name)
        except AttributeError:
            parser = MainParser

        return parser(raw_whois)


class EuParser(MainParser):
    attributes_regex = {
        'domain_name': r'Domain: *([^\n\r]+)',
        'name_servers': r'Name servers: *([^\n\r]+)\s*([^\n\r]*)',
        'registrar': r'Registrar: *Name: *([^\n\r]+)',
    }


class RuParser(MainParser):
    attributes_regex = {
        'creation_date': 'created: *(.+)',
        'domain_name': 'domain: *(.+)',
        'expiration_date': 'paid-till: *(.+)',
        'name_servers': 'nserver: *(.+)',
        'org': 'org: *(.+)',
        'registrar': 'registrar: *(.+)',
        'status': 'state: *(.+)',
    }


class FiParser(MainParser):
    attributes_regex = {
        'creation_date': 'created\.*: *([\S]+)',
        'domain_name': 'domain\.*: *([\S]+)',
        'expiration_date': 'expires\.*: *([\S]+)',
        'name_servers': 'nserver\.*: *([\S]+) \[\S+\]',
        'status': 'status\.*: *([\S]+)',
    }


class IoParser(MainParser):
    attributes_regex = {
        'domain_name': 'Domain\s*: *(.+)',
        'expiration_date': 'Expiry\s*: *(.+)',
        'name_servers': 'NS \d?\s*: *(.+)',
        'registrar': r'Check for \'[\w\.]*\' --- (.+)',
        'status': 'Status\s*: *(.+)',
    }
