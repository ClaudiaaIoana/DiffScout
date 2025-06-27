# setup.py
from setuptools import setup, find_packages

setup(
    name='DiffScout',
    version='0.1.0',
    description='Automated Differential Cryptanalysis Tool',
    author='Dascalescu Claudia',
    author_email='claudia.dascalescu2909@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    python_requires='>=3.7',
)
