import os

from setuptools import setup, find_packages

version_file = os.path.join(
    os.path.dirname(__file__),
    "vc2_conformance_data",
    "version.py",
)
with open(version_file, "r") as f:
    exec (f.read())  # noqa: E211

readme_file = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme_file, "r") as f:
    long_description = f.read()

setup(
    name="vc2_conformance_data",
    version=__version__,  # noqa: F821
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/bbc/vc2_conformance_data",
    author="BBC R&D",
    description=(
        "Test data and images for the conformance testing software "
        "for the SMPTE ST 2042-1 VC-2 professional video codec."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-3.0-only",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="vc2 dirac dirac-pro conformance data",
    install_requires=[],
    entry_points={"console_scripts": []},
)
