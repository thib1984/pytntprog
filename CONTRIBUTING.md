# Work

git clone https://github.com/thib1984/pytntprog.git
cd pytntprog 
rm -rf pytntprog_env #clean env if necessary
python3 -m venv pytntprog_env
source pytntprog_env/bin/activate
#work!
pip3 install .
pytntprog [...] #to retest
deactivate

python3 -m build && python3 -m twine upload dist/* #to publish to pypi
