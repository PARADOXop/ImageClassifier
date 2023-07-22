import logging
import os
import sys
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
package_name = 'DEEPCNNClassifier'

list_of_file = [
    '.github/workflows/.gitkeep',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    'config.config.yaml',
    'dvc.yaml',
    'params.yaml',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'research/trails.iypnb'

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'Creating directory: {filedir} for file : { filename}')
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'creating empty file : {filepath}')
    else:
        logging.info(f'file {filepath} already exist')