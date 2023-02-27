import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='myawesomepackage',
    version='0.0.3',
    author='Joaquin Sanchez',
    author_email='sanchezjoaquin1995@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/joacosnchz/test-python-package',
    project_urls = {
        "Bug Tracker": "https://github.com/joacosnchz/test-python-package/issues"
    },
    license='MIT',
    packages=['myawesomepackage'],
    install_requires=[]
)
