# Description
How to create your own python package to be installed with pypi privately

# Installation
1. Open terminal
2. Run `python setup.py bdist_wheel`
3. Run `pip install dist/*.whl`
4. Run `python example/index.py`
5. To uninstall: `pip uninstall myawesomepackage`
