from setuptools import setup, find_packages

setup(
    name="boat_api",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest",
        "setuptools",
    ],
)
