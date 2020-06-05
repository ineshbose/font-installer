from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='font_installer',
    version="0.1.2",
    packages=find_packages(),
    install_requires=requirements,

    author='Inesh Bose',
    desription='Install fonts from popular font sites!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL',
    url='https://github.com/ineshbose/font-installer',

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],
    keywords='font downloader google dafont',
    entry_points={
        "console_scripts": [
            "font-installer = font_installer.download:main",
        ],
    }
)