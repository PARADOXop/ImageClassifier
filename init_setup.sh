echo [$(date)]: 'START'
echo [$(date)]: 'CREATING ENV WITH PYTHON 3.8'
conda create --prefix deep_pro python=3.8 -y
echo [$(date)]: 'ACTIVATING THE ENV'
source activate deep_pro
echo [$(date)]: 'INSTALLING THE DEV REQUIREMENTS'
pip install -r requirements_dev.txt
echo [$(date)]: 'END'