import setuptools
with open('README.md', 'r', encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0.1'

REPO_NAME = 'DEEPCNNClassifier',
AUTHOR_USER_NAME = 'PARADOXop',
SRC_REPO = 'DEEPCNNClassifier',
AUTHOR_EMAIL = 'RAVIRAJKUKADE11@GMAIL.COM'

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= 'A small python package for CNN',
    long_description= long_description,
    long_description_content = 'text/markdown',
    url= f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    package_dir= ('': "src")
    packages=setuptools.find_packages(where='src')
    
    )