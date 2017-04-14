from .parser import MainParser
from subprocess import check_output, TimeoutExpired

__author__ = 'Rustem Sayargaliev'
__version__ = '0.0.2'


def whois(domain, fail_silently=False):
    try:
        bytes_out = check_output(['whois', domain], timeout=10)
    except TimeoutExpired:
        if not fail_silently:
            raise
        bytes_out = ''
    out = bytes_out.decode(encoding='utf8')
    return MainParser.load(domain, raw_whois=out)
