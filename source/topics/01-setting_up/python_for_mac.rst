.. _python_for_mac:

***************************
Setting Up macOS for Python
***************************

==================
Getting The Tools
==================

macOS sometimes comes with Python out of the box, but not the full setup you'll need for development or this class. It also doesn't have the latest version, so we recommend installing a new version.

.. note:: If you use ``macports`` or ``homebrew`` to manage \*nix software on your machine, feel free to use those for ``python``, ``git``, etc, as well. But make sure you have Python 3.9 or greater. If not, then read on.

Terminal
---------

You will need a command line terminal. The built-in "terminal" application works fine. Find it in::

    /Applications/Utilities/Terminal

Drag it to the dock to access more easily.

Python
------

While macOS oftentimes provide Python out of the box, it tends not to have the latest version, and you really don't want to mess with the system installation. So we recommend installing an independent installation from ``python.org``.

Download the latest release of Python installer from Python.org:

https://www.python.org/downloads/

NOTE: As of this writing, version 3.13.0 was just released -- it will work fine. But we will not be using any 3.13 features in this course, and examples will generally refer to Python 3.9 -- so anything between 3.9 and 3.13 should be good.

Double click the installer and follow the prompts. The defaults are your best bet. Simple as that.

Installing Python on macOS does NOT install a ``python`` command, but rather a ``python3`` command. You can type ``python3`` all the time or you can create an alias, like this:

.. code-block:: bash

    alias python='python3'

You can add this to your ``.zsh_profile`` file.

The reason for setting an alias rather like this is because some installations of macOS include Python already and they map the ``python`` command to the included version of Python. You do not want to change the system version of Python.

Once you have set an alias then you should be able to type ``python`` at the command prompt and get something like:

.. code-block:: bash

    $ python
    Python 3.12.5 (main, Aug  9 2024, 08:49:33) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

This is the Python interpreter.

Type ``ctrl+D`` to get out (or ``exit()``)

.. note:: If all this is confusing to you -- take heart -- you will get used to it. And in the meantime, you can simply type ``python3`` when you want to run python.

pip
---

``pip`` is the Python package installer. It should be installed with Python and generally the version that comes with Python is up to date enough that you won't need to install a newer version. Just make sure you can run ``pip`` and get back its help page.

.. code-block:: bash

    $ python -m pip

Using pip:
----------

To use pip to install a package, you invoke it with this command::

    $ python3 -m pip install the_name_of_the_package

Where ``python3`` is the command you use to invoke the Python you want to use.

**NOTE:** You will frequently see advice to use pip like so::

    $ pip install something_or_other

This often works, but also can invoke the *wrong* version of pip. This command::

    $ python3 -m pip install something_or_other

Calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of Python that you are running.

iPython
-------

One package we are going to use in the program from the beginning is ``iPython``. You can install it with ``pip`` like so::

    $ python3 -m pip install ipython

(It will install a LOT...)

Now you should now be able to run ``iPython``:

.. code-block:: ipython

    $ ipython
    Python 3.12.5 (main, Aug  9 2024, 08:49:33) [Clang 15.0.0 (clang-1500.3.9.4)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]:

Which you can also get out of with ``ctrl+D`` or ``exit()``

git
---

Git is a source code version control system. It is not strictly related to Python, but it (or a similar system) is a critical tool for software development in general, and it is very widely used in the Python community. We will be using it, along with the GitHub Classroom service, in the program to hand in assignments and support code review.

You will need a git client. The GitHub GUI client may be nice; I honestly don't know. However, we will be using the command line client in class.

There are a couple of options for a command line client.

Perhaps the easiest way, particularly if you need a compiler for any other reason, is to get git as part of the XCode command line tools, You can install XCode from the App Store. But be forewarned -- it is a VERY big download: 11.2GB!

After you have installed XCode, the ``git`` command should work.

.. code-block:: bash

    $ git --version
    git version 2.24.3 (Apple Git-128)

Testing it out
--------------

To be ready for this course, you need to have, all available from the command line:

- python
- pip
- iPython
- git

To try it out, you should be able to run all of the following commands, and get something like the results shown:

(Recall that you can get out of the python or iPython command lines with ``quit()`` or ``ctrl+Z``. If that doesn't work, try ``ctrl+D``.)

For Python:
...........

.. code-block:: bash

    $ python3
    Python 3.12.5 (main, Aug  9 2024, 08:49:33) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

For iPython:
............

.. code-block:: bash

    $ ipython
    Python 3.12.5 (main, Aug  9 2024, 08:49:33) [Clang 15.0.0 (clang-1500.3.9.4)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]:

For pip:
........

.. code-block:: bash

    $ python3 -m pip --version
    pip 24.2 from /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pip (python 3.12)

Note that when you ask pip for ``--version`` it tells you which version of python it is "connected" to.
Make sure that's the one you expect!

For git:
........

.. code-block:: bash

    $ git --version
    git version 2.39.3 (Apple Git-146)

If those commands all run -- you are all set!
