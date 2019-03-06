from setuptools import setup, find_packages


APP_NAME = 'cliapp'
VERSION = '0.1.0'
AUTHOR = 'James Hibbard'
AUTHOR_EMAIL = 'James.Hibbard@seattlechildrens.org'

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="cliapp is an example python project",
    license="MIT",
    install_requires=[
        'Click==7.0',
        'requests==2.21.0',
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        cliapp=cliapp.runner:cli
    ''',
)
