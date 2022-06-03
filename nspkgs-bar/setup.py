from setuptools import find_namespace_packages, setup

setup(
    name="nspkgs-bar",
    version="1.0.0",
    url="https://github.com/safl/nspkgs/",
    packages=find_namespace_packages(include=["nspkgs.*"]),
    zip_safe=False,
)
