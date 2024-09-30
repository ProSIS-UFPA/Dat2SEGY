from setuptools import setup, find_packages

setup(
    name='Dat2SEGY',
    version='0.1.0',
    description='Dat 2 SEGY format convert',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Wilson Oliveira',
    author_email='wilson.oliveira.souza@ig.ufpa',
    Organization: 'ProSis-LAB'
    url='https://github.com/ProSIS-UFPA/Dat2SEGY',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Working in Progress',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.7',  # Specify minimum Python version
    zip_safe=False,
)
