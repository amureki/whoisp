from whoisp import whois


def test_whoisp():
    whois_data = whois('yandex.ru').parsed

    assert whois_data
    assert whois_data.get('domain_name')
    assert whois_data.get('expiration_date')
