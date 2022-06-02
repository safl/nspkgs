Native namespace package example
================================

This is an example of using Native namespace packages are described here:

* https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

In this example the namespace is ``nspkgs``, two examples are provided
implementing as described in the docs:

* ``nspkgs-foo``
* ``nspkgs-bar``

Here is what the packaging structure looks like::

  .
  ├── LICENSE
  ├── README.rst
  ├── example-bar.py
  ├── example-foo.py
  ├── nspkgs-bar
  │   ├── Makefile
  │   ├── nspkgs
  │   │   └── bar
  │   │       ├── __init__.py
  │   │       └── jazz.py
  │   ├── pyproject.toml
  │   └── setup.py
  └── nspkgs-foo
      ├── Makefile
      ├── nspkgs
      │   └── foo
      │       ├── __init__.py
      │       └── jazz.py
      ├── pyproject.toml
      └── setup.py

So basically, with the "implicit" namespace packaging introduced in Python 3.3,
it is just "do not add a ``__init__`` in ``nspkgs`` directory and use
``find_namespace_packages()`` instead of ``find_packages()`` in ``setup.py``.

Try installing them and running their associated ``example-bar.py`` and
``example-foo.py``. This covers what it does. However, one can then take things
a bit futher:

* Create a **meta** package named ``nspkgs`` with ``install-requires`` of
  ``nspkgs-foo`` and ``nspkgs-bar``. Then, the user just does ``python3 -m pip
  install nspkgs`` and all implementations are installed.

* Create a **common** package named ``nspkgs`` containing another subpackage
  with common utilities.

Python **namespace** packages are super convenient for various reasons. As
subsets of a larger project can have different build and runtime dependencies,
have different version numbers / updates, while still share a codebase for
common functionality.

This is example was crafted for the purpose of providing a skeleton for a
namespace package providing a C-language binding packages, with distribution
packages for ``ctypes`` and another for ``Cython``.
