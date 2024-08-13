from setuptools import find_packages, setup
from typing import List

def install_libs(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Ai Agents Basic',
    version='0.0.1',
    author ='Kashish Rajput',
    author_email = 'kashishrajput2000@gmail.com',
    packages = find_packages(),
    install_requires = install_libs('requirements.txt')
)