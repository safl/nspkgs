Python Packaging: native namespace package example
==================================================

This is an example of Python packaging using **native namespace packages**,
this method is one of the three methods for creating **namespace packages** as
described here:

* https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

The documentation refers to a **native namespace package** example here:

* https://github.com/pypa/sample-namespace-packages/tree/master/native

The Python Packaging Authority (**pypa**) example is excellent, because it is
minimal, nothing to get confused about.

When experimenting with namespace packages, and writing up the example in this
repository, I had not seen the official **pypa** example. I wish I did.
However, the example here does a bit more, i would recommend reading the
**pypa** example first then this one here.

In this example the namespace is ``nspkgs``, three package-examples are
provided, start with these:

* ``nspkgs-foo``
* ``nspkgs-bar``

The essence is, with the **implicit** namespace packaging introduced in Python
3.3, it is just a matter of:

* Do **not** add a ``__init__.py`` in the top-level namespace directory
* Use ``find_namespace_packages()`` instead of ``find_packages()`` in
  ``setup.py``.
* Disable ``zip_safe``

Try installing the package-examples and run their associated ``example-bar.py``
and ``example-foo.py``. This covers what it does. However, one can then take
things a bit futher:

* Create a **core**/**common** package named ``nspkgs`` containing a subpackage
  with default implementation and common utilities. An example of that is
  provided in ``nspkgs-core``.

* Create a **meta** package named ``nspkgs`` with ``install-requires`` of
  ``nspkgs-foo`` and ``nspkgs-bar``. Then, the user just does ``python3 -m pip
  install nspkgs`` and all implementations are installed.

Python **namespace** packages are super convenient for various reasons. As
subsets of a larger project can have different build and runtime dependencies,
have different version numbers / updates, while still share a codebase for
common functionality.

This is example was crafted for the purpose of providing a skeleton for a
namespace package providing a C-language binding packages, with distribution
packages for ``ctypes`` and another for ``Cython``.

**note:** In case you are using ``pytest`` discovery via packages, then take
note that the "top-level" of the namespace cannot be searched, one has to
specify the subpackages, e.g. ``python3 -m pytest --pyargs nspkgs.foo``
