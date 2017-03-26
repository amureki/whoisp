# whoisp

[![Travis](https://api.travis-ci.org/amureki/whoisp.svg?branch=master)](https://travis-ci.org/amureki/whoisp)
[![Version](https://img.shields.io/pypi/v/whoisp.svg)](https://pypi.python.org/pypi/whoisp/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/amureki/whoisp/master/LICENSE)


Python wrapper for bash `whois` command.
Supports Python 2.7, 3.5, 3.6

### Installation

	pip install whoisp


### Usage

    from whoisp import whois

    whois_data = whois('yandex.ru').parsed
    whois_data.get('domain_name')
    > ['YANDEX.RU']
    whois_data.get('expiration_date')
    > ['2017-09-30T21:00:00Z']

### Testing

    pip install -r requirements_test.txt
    pytest

or

    pip install tox
    tox
