from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n','') for req in requirements]


        return requirements


setup(
    name='waferfault',
    version='0.0.1',
    author='Rahul',
    author_email='272rahulrai@GMAIL.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()





)