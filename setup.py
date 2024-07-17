from setuptools import setup, find_packages

setup(
    name='my_leetcode_tracker',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'matplotlib',
        'pandas',
    ],
)
