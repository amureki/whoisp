import os

import pytest

from whoisp.parser import MainParser

TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data')


def domain_list():
    domains = [domain for domain in os.listdir(TEST_DATA_PATH) if not domain.startswith('.')]
    return domains


@pytest.mark.parametrize(
    'zone', domain_list()
)
def test_parser(zone):
    domain = 'test.{}'.format(zone)
    zone_file = os.path.join(TEST_DATA_PATH, zone)
    with open(zone_file) as f:
        raw_whois = f.read()

    parser = MainParser.load(domain, raw_whois=raw_whois)
    whois_data = parser.parsed
    assert any(whois_data.values())
