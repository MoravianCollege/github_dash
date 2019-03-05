
from setuptools import setup, find_packages

setup(
    name="github_dash",
    packages=find_packages('src'),
    package_dir={'': 'src'}
)

setup(
    name="github_collect",
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
