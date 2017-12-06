from setuptools import setup

setup(
    name='sqlalchemy-vertica-python-eighty20',
    version='0.1.2',
    description='Vertica dialect for sqlalchemy using vertica_python',
    long_description=open("README.rst").read(),
    license="MIT",
    url='https://github.com/Eighty20/sqlalchemy-vertica-python',
    download_url = 'https://github.com/Eighty20/sqlalchemy-vertica-python/tarball/0.1.2',
    author='Eighty20',
    author_email='info@eighty20.co.za',
    packages=[
        'sqla_vertica_python',
    ],
    entry_points="""
    [sqlalchemy.dialects]
    vertica.vertica_python = sqla_vertica_python.vertica_python:VerticaDialect
    """,
    install_requires=[
        'vertica_python'
    ],
)

