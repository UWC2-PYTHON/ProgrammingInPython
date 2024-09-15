.. _exercise_mailroom_package:

###############################
Mailroom -- as a Python Package
###############################

The mailroom program is a small but complete system. If you wanted to make it available for others to test and run, making a "proper" python package is a great idea. Making a package of it will also make it easier to develop and test, even if you are the only one to use it.

Code Structure
==============

Start with your existing version of mailroom.

It may already be structured with the "logic" code distinct from the user interface. (Yes, a command line *is* a user interface.) But you may have it all in one file. This isn't *too* bad for such a small program, but as a program grows, you really want to keep things separate, in a well organized package.

The first step is to re-structure your code into separate files:

- One (or more) for the logic code: the code that manipulates the data
- One for the user-interface code: the code with the interactive loops and all the "input" and "print" statements
- One (or more) for the unit tests.

You should have all this pretty distinct after having refactored for the unit testing. If not, this is a good time to do it!

In addition to those three, you will need a single function to call that will start the program. That can be defined in a new file, as a "script", but for something as simple as this, it can be in with your interface code. That file can then have an ``if __name__ == "__main__"`` block which should be as simple as:

.. code-block:: python

    if __name__ == "__main__":
        main()


Making the Package
==================

Put all these in a python package structure, something like this::

    └── mailroom
        ├── pyproject.toml
        └── mailroom
            ├── __init__.py
            ├── cli.py
            ├── model.py
            └── tests
                ├── __init__.py
                ├── test_cli.py
                └── test_model.py

You will need to import the logic code from model.py in the cli code in order to use it.

You can wait until you learn about mocking to write the code in test_cli.py, so you can leave that out for now.

Now write a ``pyproject.toml`` file to support the installation of your package.

Making the Top-Level Script Runnable
------------------------------------

To get the script installed you have two options. I used to prefer the more straightforward one, `the project.scripts configuration <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>`_.

Using this configuration you will end up with an executable Python script that starts your program. The configuration to achieve this should look something like this:

.. code-block:: toml

    [project.scripts]
    mailroom = "mailroom.cli:main"

The basic syntax is pretty straightforward. You want a program called ``mailroom`` that calls the ``main`` function in the the ``mailroom.cli`` module. That's it. You can have multiple entries if you want to have multiple scripts. Just follow the same syntax.

``setuptools`` will create a wrapper script with the name given, and that wrapper will call the function in the module that is specified.

Once this is all set up, and you install the package, either in editable mode or not:

.. code-block:: bash

    $ python3 -m pip install -e .

You should then be able to type "mailroom" at the command line and have your program run.

Testing your Package
--------------------

When you are done, you should be able to both install your package fully:

.. code-block:: bash

    $ python3 -m pip install .

Or in "editable" mode:

.. code-block:: bash

    $ python3 -m pip install -e .

When that is done, you should be able to run the top-level script from anywhere:

.. code-block:: bash

    $ mailroom

And run the test from within the package:

.. code-block:: bash

    $ pytest --pyargs mailroom

Or you can run the tests from the test dir as well.

If you installed in editable mode, then you can update the code and re-run the tests or the script, and it will use the new code right away.
