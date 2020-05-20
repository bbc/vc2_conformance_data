import os

from setuptools import setup, find_packages

version_file = os.path.join(
    os.path.dirname(__file__), "vc2_conformance_data", "version.py",
)
with open(version_file, "r") as f:
    exec (f.read())  # noqa: E211

setup(
    name="vc2_conformance_data",
    version=__version__,  # noqa: F821
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/bbc/vc2_conformance_data",
    author="BBC R&D",
    description=(
        "Test data and images for the conformance testing software "
        "for the SMPTE ST 2042-2 VC-2 professional video codec."
    ),
    license="GPLv2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords="smpte-RP-2042-3 vc2 dirac dirac-pro conformance data",
    install_requires=[],
    entry_points={"console_scripts": []},
)
