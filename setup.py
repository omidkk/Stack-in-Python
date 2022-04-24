from setuptools import find_namespace_packages, setup

setup(
    name="y24-interview-q1",
    version="1.0.0",
    packages=find_namespace_packages(include=["src"]),
    author="Omidkk",
    description="Stack data structure",
    classifiers=["Programming Language :: Python :: 3.8"],
    test_suite="tests",
)
