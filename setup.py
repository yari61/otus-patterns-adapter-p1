from setuptools import setup, find_packages

with open("requirements.txt", mode="r") as requirements_file:
    requirements = [line.split("#")[0]
                    for line in requirements_file.read().split("\n")]

setup(
    name="matrix-sum",
    description="",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=requirements
)
