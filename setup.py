from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT='-e .'

def get_requirments(file_path:str)->List[str]:
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        
        if(HYPER_E_DOT in requirements):
            requirements.remove(HYPER_E_DOT)
        

setup(
    name='ML project',
    version='0.0.1',
    author='Rakesh',
    author_email='rockersinfo@gmail.com',
    packages=get_requirments('requirements.txt'),
    install_requires=['numpy','panda'],
)
