.. _packaging:

######################
Packages and Packaging
######################

Packages, Modules, Imports, Oh My!
==================================

Before we get started on making your own package -- let's remind ourselves about packages and modules, and importing.

Modules
-------

A python "module" is a single namespace, with a collection of values:

* functions
* constants
* class definitions
* really any old value

A module usually corresponds to a single file: ``something.py``

Packages
--------

A "package" is essentially a module, except it can have other modules -- and indeed other packages -- inside it.

A package usually corresponds to a directory with a file in it called ``__init__.py`` and any number of python files or other package directories::

    a_package
        __init__.py
        module_a.py
        a_sub_package
            __init__.py
            module_b.py

The ``__init__.py`` can be totally empty -- or it can have arbitrary python code in it. The code will be run when the package is imported -- just like a module.

Modules inside packages are *not* automatically imported. So, with the above structure::

    import a_package

Will run the code in ``a_package/__init__.py``. Any names defined in the ``__init__.py`` will be available in::

    a_package.a_name

But::

    a_package.module_a

Will not exist. To get submodules, you need to explicitly import them like so::

    import a_package.module_a

More on Importing
-----------------

You usually import a module like this:

.. code-block:: python

    import something

Or:

.. code-block:: python

    from something import something_else

Or a few names from a package:

.. code-block:: python

    from something import (name_1, name_2, name_3, x, y)

You also can optionally rename stuff as you import it:

.. code-block:: python

    import numpy as np

This is a common pattern for using large packages -- maybe with long names -- and not having to type a lot.

``import *``
------------

.. code-block:: python

    from something import *

Means: "import all the names in the module, "something".

You really don't want to do that! It is an old pattern that is now an anti-pattern.

But if you do encounter it, it doesn't actually import all the names -- it imports the ones defined in the module's ``__all__`` variable.

``__all__`` is a list of names that you want ``import *`` to import. So the module author can control it, and not accidentally override built-ins or bring a lot of extraneous names into your namespace.

But really:

.. centered:: **Do NOT use** ``import *``

Relative Imports
----------------

Relative imports were added with PEP 328: https://www.python.org/dev/peps/pep-0328/

The final version is described here: https://www.python.org/dev/peps/pep-0328/#guido-s-decision

This gets confusing! There is a good discussion on Stack Overflow here: `Relative Imports for the Billionth Time <http://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time>`_

Relative imports allow you to refer to other modules relative to where the existing module is in the package hierarchy, rather than in the entire python module namespace. For instance, with the following package structure::

    package/
        __init__.py
        subpackage1/
            __init__.py
            moduleX.py
            moduleY.py
        subpackage2/
            __init__.py
            moduleZ.py
        moduleA.py

You can write in ``moduleX.py``:

.. code-block:: python

    from .moduleY import spam
    from . import moduleY
    from ..subpackage1 import moduleY
    from ..subpackage2.moduleZ import eggs
    from ..moduleA import foo
    from ...package import bar
    from ...sys import path

This is similar to command line shells where:

* "." means "the current package"
* ".." means "the package above this one"

Note that you have to use the ``from`` form of import when using relative imports.

Caveats
.......

* You can only use relative imports from within a package.
* You can not use relative imports from the interpreter.
* You can not use relative imports from a top-level script. (i.e. if ``__name__`` is set to ``__main__``. So the same python file with relative imports can work if it's imported, but not if it's run as a script.)

The alternative is to always use absolute imports:

.. code-block:: python

    from package.subpackage import moduleX
    from package.moduleA import foo

Advantages of Relative Imports
..............................

* The package does not have to be installed.
* You can move things around and not much has to change.

Advantages of Absolute Imports
..............................

* Explicit is better than implicit.
* Imports are the same regardless of where you put the package.
* Imports are the same in package code, command line, tests, scripts, etc.

There is debate about which is the "one way to do it" -- a bit unpythonic, but you'll need to make your own decision.

``sys.modules``
---------------

``sys.modules`` is simply a dictionary that stores all the already imported modules. The keys are the module names, and the values are the module objects themselves.

.. note:: Remember that everything in Python is an object, including modules. So they can be stored in lists and dict, assigned names, even passed to functions, just like any other object. They are not often used that way, but they can be.

.. code-block:: ipython

    In [3]: import sys

    In [4]: type(sys.modules)
    Out[4]: dict

    In [6]: sys.modules['textwrap']
    Out[6]: <module 'textwrap' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/textwrap.py'>

    In [10]: [var for var in vars(sys.modules['textwrap']) if var.startswith("__")]
    Out[10]:
    ['__spec__',
     '__package__',
     '__loader__',
     '__doc__',
     '__cached__',
     '__name__',
     '__all__',
     '__file__',
     '__builtins__']

You can access the module through the ``sys.modules`` dict:

.. code-block:: ipython

    In [12]: sys.modules['textwrap'].__file__
    Out[12]: '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/textwrap.py'

Which is the same as:

.. code-block:: ipython

    In [13]: import textwrap

    In [14]: textwrap.__file__
    Out[14]: '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/textwrap.py'

    In [15]: type(textwrap)
    Out[15]: module

    In [16]: textwrap is sys.modules['textwrap']
    Out[16]: True

So, more or less, when you import a module, the interpreter:

* Looks to see if the module is already in ``sys.modules``.
* If it is, it binds a name to the existing module in the current module's namespace.
* If it isn't:

    - A module object is created
    - The code in the file is run
    - The module is added to sys.modules
    - The module is added to the current namespace

Implications of Module Import Process
-------------------------------------

* The code in a module only runs once per program run.
* Importing a module again is cheap and fast.
* Every place your code imports a module it gets the *same* object

    - You can use this to share "global" state where you want to.

* If you change the code in a module while the program is running -- the change will **not** show up, even if re-imported.

    - That's what ``importlib.reload()`` is for.

The module search path
----------------------

The interpreter keeps a list in ``sys.path`` of all the places that it looks for modules or packages when you do an import:

.. code-block:: python

    import sys
    for p in sys.path:
        print(p)

You can manipulate that list to add or remove paths to let python find modules in a new place.

Every module has a ``__file__`` name that points to the path it lives in. This lets you add paths relative to where you are, etc.

.. note:: It's usually better to use your package manager's "develop" mode (e.g. ``pip install -e``) instead of messing with ``sys.path``. See below for examples.

.. note:: One "gotcha" in Python is "name shadowing". The interpreter automatically adds the "current working directory" to ``sys.path``. This means you can start the interpreter and just ``import something`` to work with your code. But if you happen to have a python file, or package, in your current working directory that's the same as an installed package, then it will get imported instead, which can lead to some odd errors. If you are getting confusing errors on import then check for python modules in your current working directory that may match an installed package.

Reloading
---------

Once loaded, a module stays loaded.

If you import it again -- usually in another module -- it will simply use the version already there rather than re-running the code.

And you can access all the already loaded modules from ``sys.modules``.

.. code-block:: ipython

    In [4]: import sys

    In [5]: sys.modules.keys()
    Out[5]: dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'posix', 'zipimport', 'encodings', 'codecs', '_codecs'

There is a lot there already!

There's no reason to, but you could import an already imported module like so:

.. code-block:: ipython

    In [10]: math = sys.modules['math']

    In [11]: math.sin(math.pi)
    Out[11]: 1.2246467991473532e-16

    In [12]: math.sin(math.pi / 2)
    Out[12]: 1.0

Python Distributions
====================

So far, we've used the Python from python.org. It works great, and supports a lots of packages via pip.

But there are also a few "curated" distributions. These provide python and a package management system for hard-to-build packages.

These are Widely used by the scipy community:

* `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ and `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
* `ActivePython <http://www.activestate.com/activepython>`_

Conda has seen a LOT of growth in the last few years. It's based on the open-source conda packaging system, and provides both a commercial curated set of packages, and a community-developed collection of packages known as conda-forge:

https://conda-forge.org/

If you are doing data science or scientific development then I recommend you take a look at Anaconda, conda and conda-forge.

Installing Packages
===================

Every Python installation has its own stdlib and ``site-packages`` folder. ``site-packages`` is the default place for third-party packages.

From Source
-----------

* ``python setup.py install`` -- though this is heading towards deprecation
* ``python -m build .`` -- the newer way for use with the newer ``pyproject.toml`` files
* With the system installer (apt-get, yum, dnf, etc.)

From Binaries
-------------

* Binary wheels -- ``pip`` should find appropriate binary wheels if they are there

A Bit of History
-----------------

In the beginning, there was the ``distutils``:

But ``distutils`` was missing some key features:

* package versioning
* package discovery
* auto-install

And then came ``PyPI`` -- the Python Package Index.

And then came ``setuptools`` with easy_install.

But that wasn't well maintained so easy_install disappeared.

Then there was ``pip`` which replaced running ``setup.py`` and ``easy_install``.

``pip`` is still there but now there is also `poetry <https://python-poetry.org/>`__ and `hatch <https://hatch.pypa.io/latest/>`__ and `uv <https://docs.astral.sh/uv/>`_ and a few others.

You can't really go wrong with pip+setuptools but you should explore other tools like poetry and uv if you want to take advantage of their additional features or workflows.

Installing Packages
-------------------

Actually, it's still a bit of a mess. It's getting better, and the mess is *almost* cleaned up.

To build packages: setuptools
.............................

* https://setuptools.readthedocs.io/en/latest/

Most folks use setuptools for everything, though poetry and uv are making headways.

To install packages: pip
........................

* https://pip.pypa.io/en/latest/installing.html

pip is basically the only package installer that you need. It comes with Python, usually, and almost always does the right thing.

For binary packages: wheels
...........................

* http://www.python.org/dev/peps/pep-0427/

You don't really need to know about wheels except to say the following. Many Python packages incorporate code written in C or C++ or Rust. Historically, when you ran "pip install" for one of these packages then pip would build the package from source. This meant you needed build tools on your host which you might not have. Python "wheels" are pre-compiled binaries created by the package maintainer for your specific operating system. This way you do not need build tools installed on your system to use these packages and they install much, much more quickly.

Final Recommendations
---------------------

First try: ``pip install``

If that doesn't work, then read the docs of the package you want to install and do what they say.

virtualenv
----------

``virtualenv`` is a tool to create isolated Python environments.

It is very useful for developing multiple applications and for keeping your system Python from being polluted with lots of packages.

See: http://www.virtualenv.org/en/latest/index.html

You can find some additional notes here: :ref:`virtualenv_section`

**NOTE:** Conda also provides a similar isolated environment system.

Building Your Own Package
=========================

The term "package" is overloaded in Python. As defined above, it means a collection of Python modules. But it often is used to refer to not just the modules themselves, but the whole collection, with documentation and tests, bundled up and installable on other systems.

Here are the very basics of what you need to know to make your own package.

Why Build a Package?
--------------------

There are a bunch of nifty tools that help you build, install and distribute packages.

Using a well structured, standard layout for your package makes it easy to use those tools.

Even if you never want to give anyone else your code, a well structured package eases development.

What is a Package?
------------------

**A collection of modules**

* ... and the documentation
* ... and the tests
* ... and any top-level scripts
* ... and any data files required
* ... and a way to build and install it...

Python Packaging Tools
----------------------

``setuptools`` -- for building and distributing packages

``pip`` -- for installing packages

``wheel`` -- for binary distributions

These are pretty much the standard now and very well maintained by The Python Packaging Authority: `PaPA <https://www.pypa.io/en/latest/>`_

This all continues to change quickly so see that site for up to date information.

Where do I go to figure this out?
.................................

The Python project maintains a really good guide which covers the packaging tools built in to Python.

* Python Packaging User Guide: https://packaging.python.org/

There is a sample project here: https://github.com/pypa/sampleproject

You can use this as a template for your own packages. It covers the latest and greatest in Python packaging as supported by a standard Python installation, including the latest ``pyproject.toml`` configuration.

.. note:: One confusion for folks new to this is that a LOT of the documentation (and tools) around packaging for Python assumes that you are writing a package that is generally useful, and you want to share it with others on PyPI. That is partly because all the people developing the tools and writing about them are doing just that. It's also harder to distribute a package properly than to simply make one for internal use, so more tools and docs are needed. But it is still useful to make a package of your code if you aren't going to distribute it, but you don't need to do everything that is recommended.

Where do I put my custom code?
..............................

If you have a collection of your own code that you want to access for various projects, make a "package" out of it so you can manage it in one place and use it in other places. **You do NOT need to put your code on PyPI.**

Most people who write code to solve problems find that they have a collection of little scripts and utilities that they want to be able to use and reuse for various projects.

You have a few options for handling your code collection:

1. Keep your code in one place and copy and paste the functions you need into each new project. **Do not do this!** It is really not a good idea to simply copy and paste code around. You will end up with multiple versions scattered all over the place and you will regret it.
2. Put your code into a single directory and add it to the ``PYTHONPATH`` environment variable. **Do not do this!** The ``PYTHONPATH`` environment variable is shared by all installs of Python on your system so it will be used by your scripts and also other scripts that are not yours.
3. Make a package.

A Python "package" is a collection of modules and scripts that you can install with ``pip``. People usually think of these as something carefully developed for a particular purpose and distributed to a wide audience. But you can also use this strategy yourself to distribute code for yourself.

But it's a much easier process than it sounds! Let's start on making our first package.

Basic Package Structure
-----------------------

::

    package_name/
        docs/
        LICENSE.txt
        CHANGELOG.md
        README.md
        pyproject.toml
        package_name/
            __init__.py
            module1.py
            module2.py
        tests/
            __init__.py
            test_module1.py
            test_module2.py

``CHANGELOG.md`` -- A log of changes with each release, written in Markdown format. There are tools that will automatically generate this but they are beyond the scope of this guide.

``LICENSE.txt`` -- The text of the license you choose. Do choose a license! It really does matter!

``README.md`` -- A description of the package using Markdown format. You could also write it using ReST format but tools like GitHub primarily support Markdown.

Those are all the "metadata" critical if you are distributing to the world. They're not so much for your own use.

``pyproject.toml`` -- The configuration file for how to build and install your package.

``bin/`` -- This is where you put top-level scripts. Some folks prefer ``scripts``. It doesn't matter.

``docs/``-- Your documentation.

``package_name/`` -- This is the main package. This is where the code goes. You should replace "package_name" with the name of your package. Be sure to make the package name unique such that it doesn't reuse a built-in Python package name.

``tests/`` -- Ths is where your unit tests should go. There are several options here that we'll go over in a moment.

Where should I put my tests?
............................

You have a few options for where to put your test code.

If your package and the test code are small and self contained then put the tests inside the package. This results in the tests being installed with the package so that they can be run after installation, like this:

.. code-block:: bash

    $ pip install package_name
    >> import package_name.tests
    >> package_name.tests.runall()

Or:

.. code-block:: bash

    $ pytest --pyargs package_name

On the other hand, if you have a lot of tests, and do not want the entire set of tests installed with the package, then you can keep it at the top level, as shown above.

The ``pytest`` project has a discussion on this here: https://docs.pytest.org/en/stable/explanation/goodpractices.html

The advantage of keeping test code self-contained, and outside of your package, is that you can have a large test suite with sample data and whatever else, and it won't bloat and complicate the installed package.

The advantage to keeping test code within the package is that your test code gets installed with the package, so users of the package can install the package and then run the tests to make sure the package is working.

Most people choose to have the tests separate from their code.

The ``pyproject.toml`` File
---------------------------

Your ``pyproject.toml`` file describes your package and tells setuptools how to build and install it. It's the `TOML syntax <https://en.wikipedia.org/wiki/TOML>`__ which may be new to you. Additionally, you may not see every project using it. However, it is a Python standard defined by `PEP 621 <https://peps.python.org/pep-0621/>`__ so it is the future.

An example:
...........

.. code-block:: toml

    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "mypackage"
    version = "3.0.0"
    description = "My fancy project."
    readme = "README.md"
    requires-python = ">=3.8"
    license = {file = "LICENSE.txt"}
    authors = [{name = "A. Random Developer", email = "author@example.com" }]
    maintainers = [{name = "A. Great Maintainer", email = "maintainer@example.com" }]

    dependencies = [
        "Django >= 5.0"
    ]

    [project.optional-dependencies]
    test = ["pytest"]


Building Your Package
---------------------

With a ``pyproject.toml`` file defined, ``pip`` can do a lot:

* Builds wheels for your project:

    .. code-block:: bash

    $ python3 -m pip wheel .

* Install your package:

    .. code-block:: bash

    $ python3 -m pip install .

The dot at the end of the command means "this directory". ``pip`` will look in the current dir for the ``pyproject.toml`` file.

Basically, rather than making a copy of your code and putting it into your project, you're making a link to your code and telling your project to use it.

.. note:: setuptools can be used by itself to build and install packages. But over the years, pip has evolved to a more "modern" way of doing things. When you install from source with pip -- it is using setuptools to do the work, but it changes things around, and installs things in a more modern, up to date, and compatible way. For much use, you won't notice the difference, but setuptools still has some old crufty ways of doing things, so it's better to use pip as a front end as much as possible.

wheels
------

Wheels are a binary format for packages.

See: http://wheel.readthedocs.org/en/latest/

It's pretty simple. It's essentially a zip archive of all the stuff that gets installed, i.e. put in ``site-packages`` when your package is installed.

A wheel file can be pure python or it can continue binary code for compiled extensions.

Wheels are compatible with virtualenv.

As shown earlier, you can building a wheel using pip, like this:

.. code-block:: bash

    $ python3 -m pip wheel .

When you are installing a package off of PyPI, you can use ``pip install packagename`` and ``pip`` will find wheels for Windows and macOS and "manylinux" or whatever operating system you're running, assuming wheels are available for it. Or you can  ``pip install --no-use-wheel`` to avoid using wheels and build the package from source.

manylinux
---------

There are a lot of Linux distributions out there. So, for a long time, there were not easily available binary wheels for Linux. How could you define a standard with all the Linux distros out there?

Enter "manylinux". No one thinks you can support all Linux distros, but it was found that you could support many of the common ones by building on an older version and restricting system libraries. This approach worked well for Canopy and conda, so PyPi adopted a similar strategy with manylinux.

See: https://github.com/pypa/manylinux

So now there are binary wheels for Linux on PyPi.

The core scipy stack is a great example. You can now ``pip install numpy`` on all three systems (Windows, macOS, and Linux) easily with pip.

PyPI
-----

The Python Package Index: https://pypi.python.org/pypi

Sometimes called "Pie Pie", sometimes called "Pie Pee Eye".

You've all used this. Running ``pip install`` searches it. Uploading your package to PyPI is beyond the scope of this document. For a tutorial on how to do so, you can follow this tutorial: https://realpython.com/pypi-publish-python-package/

Under Development
------------------

Working with your code in develop mode -- also known as an "editable install" -- is *really* *really* nice:

.. code-block:: bash

    $ python -m pip install -e .

The e stands for "editable". The "dot" is still required.

Installing in this way puts links into the Python installation to your code, so that your package is installed, but any changes to your source code will immediately take effect in the installation.

This way all your test code, and client code, etc, can all import your package the usual way with no ``sys.path`` hacking or modifications to ``PYTHONPATH``.

It's great to use it for anything more than a single file project.

Running Tests
-------------

It can be a good idea to set up your tests to be run from ``setup.py``

So that you (or your users) can:

.. code-block:: bash

    $ pip install ".[test]"
    $ pytest

If you want to add default options to pytest you can add those to your ``pyproject.toml`` file like this:

.. code-block:: toml

    [tool.pytest.ini_options]
    addopts = "--cov --cov-report html --cov-fail-under 95"

Handling Version Numbers
------------------------

There is one key rule in software: never put the same information in more than one place!

With a Python package, you want this to return a version string:

.. code-block:: python

    import the_package

    the_package.__version__

You might expect a string like this: ``1.2.3``

Using ``__version__`` is not a requirement, but it is a very commonly used convention -- *use it*!

But you also need to specify it in the ``pyproject.toml``:

.. code-block:: toml

    [project]
    name = "mypackage"
    version = "3.0.0"

Not Good.

My Solution
...........

Put the version in the ``pyproject.toml``, as shown above.

Then write a function that will get the version and put that into your program, like this:

.. code-block:: python

    import importlib.metadata

    def version(package: str) -> str:
        try:
            return importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            return "0.0.0"

    __version__ = version(__name__)

You can also have scripts that automatically update the version number in whatever places that it needs to. For example:

* https://commitizen-tools.github.io/commitizen/
* https://github.com/warner/python-versioneer

You can hook commitizen into your project with git hooks so that it enforces conventions and bumps your version number correctly in every location based on your release.

Semantic Versioning
-------------------

Another note on version numbers.

The software development world, for the most part, has established a standard for what version numbers mean. This standard is known as semantic versioning. This is helpful to users, as they can know what to expect they upgrade.

In short, with a x.y.z version number:

x is the Major Version. It could mean changes in API, major features, etc. Changes in the major version are likely to be incompatible with previous versions.

y is the Minor Version. Some features were added features, etc, but they should be backwards compatible.

z is the "Patch" Version. This is for bug fixes, etc. that should be fully compatible.

Read all about it: http://semver.org/

There is a related versioning scheme that is appearing more often called Calendar Versioning where you bump the version based on when you released the software.

You can read about calendar versioning, too: https://calver.org/

Tools to Help
--------------

Tox is great for automating testing in Python. We won't go into it here but it's pretty popular.

https://tox.readthedocs.io/en/latest/

Dealing with Data Files
-----------------------

Oftentimes a package will require some files that are not Python code. In that case, you need to make sure the files are included with the package some how.

With the ``pyproject.toml`` file the easiest way to do that is with this syntax:

.. code-block:: toml

    [tool.setuptools]
    # If there are data files included in your packages that need to be installed, specify them here.
    package-data = {"sample" = ["*.dat"]}

This is a dict with the keys being the package(s) you want to add data files to. This is required, as a single ``pyproject.toml`` file can install more than one package. The value following the key is a list of filenames, *relative to the package*.

This is described more here: https://setuptools.pypa.io/en/stable/userguide/datafiles.html

.. note:: Debugging package building can be kind of tricky. If you install the package, and it doesn't work, what went wrong?!? One approach that can help is to "build" the package, separately from installing it. pip provides a wheel command: ``pip wheel .`` that builds your package in place. It will create a ``build`` directory, and in there you can see your package as it will be deployed. So you can look there and see if your data files are getting included, and everything else about the package.

Now you'll need to write your code to find that data file. You can do that by using the ``importlib.resources`` package built-in to Python. See: https://docs.python.org/3/library/importlib.resources.html

.. code-block:: python

    import importlib.resources

    file_path = importlib.resources.files(__name__) / "mydata.csv"

You can use the ``__name__`` magic value to get the name of the current module or you can construct it by hand.

Command Line Scripts
--------------------

If your scripts are Python files then the best way to make them accessible is to use "entry points". Entry points can provide a number of functions, but one of them is to make console scripts. Here is how you would add it to your ``pyproject.toml`` file:

.. code-block:: toml

    [project.scripts]
    example = "example:main"

What this does is tell setuptools to make a little wrapper program called "example" that will start up Python, and run the function called ``main`` in the ``example`` module.

Getting Started With a New Package
----------------------------------

For anything but a single-file script (and maybe even then):

1. Create the basic package structure
2. Write a ``pyproject.toml`` file
3. ``pip install -e .``
4. Put some tests in the ``test`` directory
5. Run ``pytest`` from the project directory

LAB: A Small Example Package
----------------------------

* Create a small package

  - package structure
  - ``pyproject.toml``
  - ``pip install -e .``
  - ``at least one working test``

* Here is a ridiculously simple and useless package to use as an example:

:download:`capitalize.zip <../examples/packaging/capitalize.zip>`

Or go straight to making a package of your mailroom project.
