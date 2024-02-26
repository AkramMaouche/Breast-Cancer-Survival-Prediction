from typing import List 
from setuptools import find_packages,setup


def get_requirments(file_path:str)->List[str]:
    requirments =[]
    HYPHEN_E='-e .'
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        [req.replace('\n','') for req in requirments]

        if HYPHEN_E in requirments : 
            requirments.remove(HYPHEN_E)

        return requirments
setup(
    name = 'Breast Cancer Survival prediction',
    version = '0.01',
    author='Akram Arilaz maouche',
    packages=find_packages(),
    author_email='akram.maouche07@gmail.com',
    install_requires = get_requirments('requirments.txt')
)