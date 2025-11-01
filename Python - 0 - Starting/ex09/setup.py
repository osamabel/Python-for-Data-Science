"""Setup configuration for ft_package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ft_package",
    version="0.0.1",
    author="obelkhad",
    author_email="obelkhad@student.1337.ma",
    description="A sample test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/osamabel/ft_package",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

