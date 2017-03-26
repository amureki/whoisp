from setuptools import setup

from whoisp import __author__, __version__

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='whoisp',
    version=__version__,
    description='simple whois parser',
    long_description=readme,
    author=__author__,
    author_email='r.sayargaliev@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/amureki/whoisp.git',
    packages=['whoisp'],
    include_package_data=True,
    zip_safe=False,
    keywords='domain,whois',
    test_suite='tests',
)
