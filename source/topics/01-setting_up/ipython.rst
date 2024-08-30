.. _ipython_resources:

*******************
iPython Interpreter
*******************

iPython is an enhanced interpreter that makes interactive experimentation at the command line much more pleasant and powerful.

The Very Basics of iPython
--------------------------

iPython can do a lot for you, but for starters, here are the key pieces you'll want to know:

Start it up:

.. code-block:: bash

    $ ipython
    Python 3.12.5 (main, Aug  9 2024, 08:49:33) [Clang 15.0.0 (clang-1500.3.9.4)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]:

This is the stuff I use every day:

* command line recall:

  - hit the "up arrow" key
  - if you have typed a bit, it will find the last command that starts the same way.

* basic shell commands:

  - ``ls``, ``cd``, ``pwd``

* any shell command:

  - ``! the_shell_command``

* pasting from the clipboard:

  - ``%paste`` (this keeps whitespace cleaner for you)

* getting help:

  - ``something?``

* tab completion:

  - ``something.<tab>``

* running a python file:

  - ``run the_name_of_the_file.py``

That's it -- you can get a lot done with those.

iPython references
------------------

* **The iPython tutorial**
    http://ipython.readthedocs.io/en/stable/interactive/tutorial.html

* **Using IPython for interactive work**
    http://ipython.readthedocs.io/en/stable/interactive/index.html -- Learn about the abilities iPython provides for interactive sessions.

* **The iPython Documentation**
    http://ipython.readthedocs.io/en/stable/ -- Use this to learn more about iPython's amazing capabilities.
