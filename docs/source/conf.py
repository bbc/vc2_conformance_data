# Configuration file for the Sphinx documentation builder.

import os
import sys

from vc2_conformance_data import __version__ as version


# -- Path setup --------------------------------------------------------------

# To find the vc2_conformance_data module
sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "Data Files for SMPTE VC-2 Conformance Testing"
copyright = "2020, SMPTE"
author = "SMPTE"

release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]

# -- Options for numpydoc/autodoc --------------------------------------------

autodoc_member_order = "bysource"

add_module_names = False

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
    "ast": ("https://greentreesnakes.readthedocs.io/en/latest/", None),
    "sympy": ("https://docs.sympy.org/latest/", None),
    # TODO: vc2_conformance
    # TODO: vc2_bit_widths
}


# -- Options for HTML output -------------------------------------------------

html_theme = "nature"

html_static_path = ["_static"]


# -- Options for PDF output --------------------------------------------------

latex_elements = {
    "papersize": "a4paper",
}
