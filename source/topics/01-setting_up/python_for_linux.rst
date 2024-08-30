.. _python_for_linux:

###########################
Setting Up Linux for Python
###########################

Python
======

For this program, you need Python 3.9 or newer.

All current Debian, Ubuntu, RaspberryPi, and Fedora distros already have the stable Python releases preinstalled.

Try the following command:

.. code-block:: bash

    $ python3
    Python 3.11.2 (main, May  2 2024, 11:59:08) [GCC 12.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Ubuntu 24.04, the latest LTS version, has Python 3.12. Debian 12, aka "bookworm", has Python 3.11. Ubuntu 22.04, the previous LTS version, has Python 3.10. So you're OK with every current version of Debian or Ubuntu. (RaspberryPi tracks Debian.)

Note that you can't type just ``python``. To work around this, add the line ``alias python=python3`` to your user's ``/home/myuser/.bashrc`` file like so:

.. code-block:: bash

    # before the change
    $ python
    -bash: python: command not found

    $ echo "alias python=python3" >> ~/.bashrc
    $ echo "alias pip=pip3" >> ~/.bashrc
    $ echo "alias ipython=ipython3" >> ~/.bashrc
    $ source ~/.bashrc

    # after the change
    $ python
    Python 3.11.2 (main, May  2 2024, 11:59:08) [GCC 12.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Alternatively, you can always remember to type ``python3`` whenever you want Python.

Note: your version number may vary, but it needs to be at least ``3.9``.

You may not have pip and ipython installed yet, but you will as you follow the instructions below.

.. note:: While your system will typically come with Python pre-installed, it is generally considered a bad idea to make changes to the installation of Python that comes with the operating system. This is where :ref:`virtual environments<virtualenv_section>` make your life easier.

Terminal
========

Every Linux box has a terminal emulator -- find and use it.

pip
===

``pip`` is the Python package installer.

To get pip, the first option is to use your system package manager, something like:

.. code-block:: bash

    # for debian and related distros
    $ sudo apt-get install python3-pip

    # for fedora and related distros
    $ sudo dnf install python3-pip

Using the system package manager to install packages might not get you the latest and greatest version but it is much safer. If you want to install the latest packages then you should use :ref:`virtual environments<virtualenv_section>`.

Using Packages:
---------------

To use your system's package manager to install a Python package, you invoke it with this command:

.. code-block:: bash

    # for debian and related distros
    $ sudo apt-get install python3-the_name_of_the_package

    # for fedora and related distros
    $ sudo dnf install python3-the_name_of_the_package

You can find the list of available packages at these links:

* https://www.debian.org/distrib/packages
* https://packages.ubuntu.com/
* https://packages.fedoraproject.org/

**NOTE:** You will frequently see advice to use pip like so::

    $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

    $ python3 -m pip install something_or_other

Calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of python that you are running (in this case python3).

Additionally, you do not want to install things directly into your system Python using pip. Always use a virtual environment!

iPython
=======

One extra package we are going to use in class is ``iPython``:

.. code-block:: bash

    # for debian and related distros
    $ sudo apt-get install ipython3

    # for fedora and related distros
    $ sudo dnf install python-ipython

You should now be able to run ``iPython``:

.. code-block:: bash

    $ ipython3
    Python 3.11.2 (main, May  2 2024, 11:59:08) [GCC 12.2.0]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

git
===

Git is likely to be there on your system already, but if not:

.. code-block:: bash

    # for debian and related distros
    $ sudo apt-get install git

    # for fedora and related distros
    $ sudo dnf install git
