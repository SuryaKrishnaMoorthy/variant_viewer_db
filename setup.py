from setuptools import setup, find_packages


APP_NAME = 'vviewer'
VERSION = '0.1.0'
AUTHOR = 'Surya Krishna Moorthy'
setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    description="vviewer is an example python project",
    license="MIT",
    install_requires=[
        "Click==7.0",
        "Flask-SQLAlchemy==2.3.2",
        "SQLAlchemy==1.3.1"
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        vviewer=vviewer.runner:cli
    ''',
)
