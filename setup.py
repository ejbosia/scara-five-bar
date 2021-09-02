from setuptools import setup

setup(
    name='linkage-tests',
    version='0.1',
    install_requires=['pytest'],
    packages=['linkages'],
    package_data={'linkages': ['tests/*', 'tests/**/*']},
)