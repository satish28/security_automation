from setuptools import setup

setup(
    name = "security_automation",
    version = "0.1.1",
    author = "Satish S",
    author_email = "satish28888@gmail.com",
    description = ("Low level security test for a web app pentest"),
    license = "MIT",
    url = "https://github.com/satish28/security_automation",
    packages = ['security_tests'],
    long_description = "Check http headers for missing security best practices, check http methods enabled in a server and perform sslscan",
    install_requires = [
        "requests>=2.9.1"
    ],
    entry_points = {
        'console_scripts' : [
            'security_automation=security_tests:main'
            ],
        }
    )
