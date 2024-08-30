.. _python_for_windows:

#############################
Setting Up Windows for Python
#############################

Getting the Tools
=================

Python
------

There are a number of Python distributions available -- many designed for easier support of scientific programming:

- Anaconda
- Python(x,y)
- etc....

But for basic use, the installer from python.org is the way to go, and that is what we will be using in this program.

https://www.python.org/downloads/

You want the installer for the latest stable version. At the time of this writing that is Python 3.12 but if a newer version has been released then that is probably OK, too, unless your instructor told you to use a specific version. There is essentially no difference for the purposes of this course.

Double click and install.

Ensure that the "Add python.exe to PATH" checkboxes at the bottom are checked.

**Add python.exe to PATH step is important!** If this is not checked then when you try to run your python code it won't be able to find the executable.

.. _git_bash:

Terminal
--------

If you are confident in your use of the "DOS Box" or "powershell", command lines, feel free to use one of those. However, your life may be easier if you install "Git Bash", as then you can follow Unix-style terminal instructions exactly, and do not have to translate. Also, your instructors are more experienced with bash.

From now on, if you hear the terms "bash", "shell", "terminal", or "command line" know that this is the application that is being referred to. We will use those terms interchangeably to mean ANY command line.

When you install Git Bash, you are installing git (and a git gui) as well, thus killing two birds with one stone! You can get Git Bash by downloading Git for Windows:

https://gitforwindows.org

Select the download button on the page and launch the downloaded executable, and then follow the prompts. On the "Choosing default editor used by Git" step it is best to select Notepad++ -- which you need to have installed first -- or some other editor that you feel comfortable using, unless you are comfortable with non-graphical editors like vim.

You can go through the rest of the prompts using default values. Once you are done, if you checked "Launch Git Bash", a terminal window should pop up - try out some commands like ``ls`` or ``git help``.

The Git Bash shell also works well for running Python. If you use the Git Bash shell, you can use the same commands as Linux and macOS users. Regardless of which shell you choose -- Command Prompt, Powershell, or Git Bash -- you will need to ensure that Python is in your environment. If you followed the instructions above then it was added to your PATH as part of the installation and everything should be working when using Command Prompt or Powershell. But it may not work with Git Bash out of the box.

In Git Bash, try running ``which python`` in bash and you should get back something like ``/c/Users/myuser/AppData/Local/Programs/Python/Python312/python``. If it says "no python" or if it says that Python is in ``/c/Users/myuser/AppData/Local/Microsoft/WindowsApp/python`` then you will need to add the correct path to your Git Bash environment. To do that, run this command::

    $ touch ~/.bash_profile

Then, from the Command Prompt -- not Git Bash -- you can run "where python" and you will see where your version of Python has been installed, for example::

    C:\Users\myuser\AppData\Local\Programs\Python\Python312\python.exe

Find the ``.bash_profile`` file in your favorite text editor. It should be in ``C:\Users\myuser\.bash_profile``. Add this line to the bottom::

    export PATH=/C/Users/myuser/AppData/Local/Programs/Python/Python312:/C/Users/myuser/AppData/Local/Programs/Python12/Scripts:$PATH

Be sure to replace ``myuser`` with your user name.

Once you have done that, you should be able to type ``python`` at the command prompt, and get something like::

    Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

This is the Python interpreter.

Type ``ctrl+Z`` to get out (or ``exit()``)

Note: if you have trouble running ``python`` command in your gitbash (it hangs), try running this instead: ``winpty python``. To avoid having to type ``winpty python`` all the time, it's strongly recommended that you create an alias like below::

    $ echo "alias python='winpty python'" >> ~/.bash_profile

You will need to close the current bash window and restart a new one to get this alias. Then from now on, you can just type ``python`` and it should work on git bash (no more hanging) as well.

git
---

If you installed Git Bash, you will already have git, both usable in the terminal and as a gui, and can safely skip this section. If not, you still need a git client. You can use the above link and install git (it will install the bash shell as well, of course, but you can use your shell of choice instead).

There is also TortoiseGit:

https://tortoisegit.org

Which integrates git with the file manager. Feel free to use this if you already have an understanding of how git works, but for the purposes of learning, it may be better to use a command line client (git Bash above).

pip
---

``pip`` is the Python package installer. It should be installed with Python and generally the version that comes with Python is up to date enough that you won't need to install a newer version. Just make sure you can run ``pip`` and get back its help page.

.. code-block:: bash

    $ python -m pip

Using pip:
----------

To use pip to install a package, you invoke it with this command::

    $ python -m pip install the_name_of_the_package

Where ``python`` is the command you use to invoke the Python you want to use .

**NOTE:** You will frequently see advice to use pip like so::

    $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

    $ python -m pip install something_or_other

Calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of Python that you are running.

iPython
--------

One extra package we are going to use from the beginning in the program is ``iPython``::

    $ python -m pip install ipython

(It will install a LOT...)

You should now be able to run ``iPython`` from the Git Bash shell or Command Prompt or PowerShell::

    $ ipython
    Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]:

We will use this in class as our default Python interpreter.

Testing it out
--------------

To be ready for the program, you need to have:
 - python
 - pip
 - iPython
 - git

All available from the command line.

To try it out, you should be able to run all of these commands, and get something like the following results, shown below.

(Recall that you can get out of the python or iPython command lines with ``quit()`` or ``ctrl+Z``. If that doesn't work, try ``ctrl+D``.)

For Python:

::

    myuser@DESKTOP-AE00AKO MINGW64 ~
    $ python
    Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> quit()

For iPython::

    myuser@DESKTOP-AE00AKO MINGW64 ~
    $ ipython
    Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: quit()

For pip::

    myuser@DESKTOP-AE00AKO MINGW64 ~
    $ python -m pip --version
    pip 24.2 from C:\Users\myuser\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)

For git::

    myuser@DESKTOP-AE00AKO MINGW64 ~i
    $ git --version
    git version 2.46.0.windows.1
