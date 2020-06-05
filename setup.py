from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='dafont_installer',
    version="0.1.1",
    packages=find_packages(),
    install_requires=requirements,

    author='Inesh Bose',
    desription='Install fonts from dafont.com!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL',
    url='https://github.com/ineshbose/dafont-installer',

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],
    keywords='dafont font downloader',
    entry_points={
        "console_scripts": [
            "dafont-installer = dafont_installer.download:main",
        ],
    }
)