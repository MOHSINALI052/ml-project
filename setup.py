from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path: str) -> List[str]:
    ''' 
    This function returns a list of requirements
    '''  
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        # Strip newlines and ignore empty lines
        requirement = [req.strip() for req in requirement if req.strip()]

    # Handle editable installation line
    if HYPEN_E_DOT in requirement:
        requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
    name='mlproject',
    version='0.0.1',
    author='mohsin',
    author_email='mohsin.raza.ali@outlook.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
)
