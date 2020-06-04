from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='dafont_installer',
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    scripts=['dafont_installer/windows.py','dafont_installer/posix.py',],

    author='Inesh Bose',
    desription='Install fonts from dafont.com!',
    long_description=long_description,
    license='GNU GPL v3',
    url='https://github.com/ineshbose/dafont-installer',

    entry_points={
        "console_scripts": [
            "dafont-installer = dafont_installer.download:main",
        ],
    }
)