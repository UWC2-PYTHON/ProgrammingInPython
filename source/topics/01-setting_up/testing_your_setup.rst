.. _testing_your_setup:

##################
Testing Your Setup
##################

If you have access to a command line, and Python installed, and a text editor or IDE ready to go, here's how you can make sure it's all working correctly.

Python Interpreter
------------------

If you have Python installed and know how to run a python file, give this a try to make sure you're all setup:

Create a file called ``install_test.py``, with the following content:

.. code-block:: python

    #!/usr/bin/env python3

    import sys
    print("This is my first python program")

    version = sys.version_info

    if version.major == 3:
        if version.minor < 9:
            print("You should be running version 3.9 or higher")
        else:
            print("I am running python {}.{} -- all good!".format(
                   version.major, version.minor))

    else:
        print("You need to run Python 3!")
        print("This is version: {}.{}".format(version.major, version.minor))

Run it with your version of python. It should result in something like this::

    This is my first python program
    I am running python 3.12 -- all good!

If you can't figure out how to run it, see: :ref:`how_to_run_a_python_file`

If you can run, it but don't get that nice "all good" message, then you either do not have Python installed, or you have the wrong version.

Go back to :ref:`setup_details`

And try again.

Run git
-------

You should be able to run git on the command line:

.. code-block:: bash

    $ git --version
    git version 2.20.1 (Apple Git-117)

It should be version >= 2

iPython
-------

``iPython`` is not critical, but it is very nice. You should be able to run it with::

    $ ipython
    Python 3.12.5 (main, Aug  9 2024, 08:49:33) [Clang 15.0.0 (clang-1500.3.9.4)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

And get something like that.

``ipython`` can be quit by typing ``quit``
