`vc2_conformance_data`: Data files for VC-2 conformance testing
===============================================================

This Python module contains data files and test pictures used by the
[`vc2_conformance`](https://github.com/bbc/vc2-conformance-software)
conformance testing software.


Setup
-----

This module has no dependencies and may be installed as usual:

    $ python setup.py install

Documentation
-------------

The documentation may be built using [Sphinx](https://www.sphinx-doc.org/) like
so:

    $ pip install -r requirements-doc.txt
    $ cd docs/
    $ make html


Development & Tests
-------------------

A test suite is provided to check that all data files can be read and are
complete.

    $ pip install -r requirements-test.txt
    $ py.test tests/

[Pre-commit](https://pre-commit.com/) hooks are provided which should be used
to ensure that all files are auto-formatted with
[black](https://github.com/psf/black) and pass the
[flake8](https://flake8.pycqa.org/en/latest/) linter checks.
