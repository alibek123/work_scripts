from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Connection to the database'
LONG_DESCRIPTION = 'My first Python package to connect to the database'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="my_connect", 
        version=VERSION,
        author="Alibek Zhumash",
        author_email="zhumash6@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        license='BSD 2-clause',
        
)