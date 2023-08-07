echo [$(date)]: "START"
echo [$(date)]: "creating env with python 3.8 version"
conda create --prefix C:\env python=3.8 -y
echo [$(date)]: "activating the environment"
conda activate C:\env
echo [$(date)]: "installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"