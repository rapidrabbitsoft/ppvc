import pathlib
import os

from setuptools import setup, find_packages

PATH = pathlib.Path(__file__).parent

# The text of the README file
README = open(os.path.join(PATH, "README.md")).read()

setup(
    name = "ppvc",
    version = "0.9.0",
    author = "Chris McMichael",
    author_email = "python@apprabb.it",
    license = "BSD-2",
    description = "A commandline utility for listing all package versions",
    long_description = README,
    long_description_content_type = "text",
    url = "https://",
    packages = find_packages(),
    py_modules = ['versions',],
    install_requires = [],
    python_requires=">=2.7",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points = """
        [console_scripts]
        ppvc=ppvc.ppvc:main
    """
)