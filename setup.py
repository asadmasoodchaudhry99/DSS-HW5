from distutils.core import setup
from setuptools import findpackages


setup(
    name="snowflake",
    version="0.1",
    author="Asad Masood",
    author_email="asad.masood.chaudhry@fau.de",
    packages=find_packages(),
    install_requirements=["numpy", "turtle"],
)