from setuptools import setup

setup(
    name='clicktest',
    version='0.1',
    py_modules=['clicktest'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clicktest=clicktest:cli
    ''',
)