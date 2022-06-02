from setuptools import find_namespace_packages, setup

setup(
    name="nspkgs-foo",
    version="1.0.0",
    url="https://github.com/safl/nspkgs/",
    packages=find_namespace_packages(include=["nspkgs.*"]),
)
