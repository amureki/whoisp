from .parser import MainParser
from subprocess import check_output

__author__ = 'Rustem Sayargaliev'
__version__ = '0.0.1'


def whois(domain):
    bytes_out = check_output(['whois', domain], timeout=10)
    out = bytes_out.decode(encoding='utf8')
    return MainParser.load(domain, raw_whois=out)
