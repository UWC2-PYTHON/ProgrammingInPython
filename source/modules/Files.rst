.. _files:

########################
File Reading and Writing
########################

Files
=====

Text Files
----------

.. code-block:: python

    f = open("secrets.txt")
    secret_data = f.read()
    f.close()

``secret_data`` is a string.

.. note:: In Python 3, files are opened by default in text mode, and the default encoding is UTF-8. This means that in the usual case, you get a proper Unicode string to work with, as UTF-8 is the most common encoding for text. Also, it is ASCII compatible, so ASCII Files with "just work". IF "Unicode" and "ASCII" mean nothing to you -- don't worry about it, just know that things will usually work for text, even non-English text. And if you get odd characters or an ``EncodingError``, then your file is not UTF-8, and it's time to Google "Python Unicode". (You can read more about Unicode here: :ref:`unicode`)


Binary Files
------------

.. code-block:: python

    f = open("secrets.bin", "rb")
    secret_data = f.read()
    f.close()

``secret_data`` is a byte string with arbitrary bytes in it. Well, not arbitrary -- whatever is in the file! See the Python ``struct`` module to unpack binary data.


File Opening Modes
------------------

.. code-block:: python

    f = open("secrets.txt", [mode])
    'r', 'w', 'a'
    'rb', 'wb', 'ab'
    'r+', 'w+', 'a+'
    'r+b', 'w+b', 'a+b'

These follow the Unix conventions, and aren't all that well documented in the Python docs. But these BSD docs make it pretty clear: http://www.manpagez.com/man/3/fopen/

**Gotcha!** ``'w'`` modes always erase the file if it already exists! If you want to add on to the end of the file then use ``'a'`` modes for "append".

Text File Notes
---------------

When opening a file, text is default.

* Line endings are translated: ``\r\n`` -> ``\n``
* Always use Unix-style line endings in your code: ``\n``

Gotcha:

* No difference between text and binary on Unix/Linux/macOS.
* But this is not true on Windows, and using the wrong file type will cause an error.

File Reading
------------

Reading part of a file:

.. code-block:: python

    header_size = 4096
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

Common Idioms
-------------

.. code-block:: python

    for line in open("secrets.txt"):
        print(line)

The file object is an iterable that iterates through the lines in a text file.

.. code-block:: python

    f = open("secrets.txt")
    while True:
        line = f.readline()
        if not line:
            break
        do_something_with_line()

We will learn more about the keyword ``with`` later -- it creates a "context manager" -- but for now, just understand the syntax and the advantage over simply opening the file:

.. code-block:: python

    with open("workfile", "r") as f:
        read_data = f.read()
    print(f.closed)  # will print True

You use ``with`` to open the file, and assign it a name. In this case we call the handle to the file ``f``. The file remains open while in the ``with`` block. At the end of the ``with`` block, the file is unconditionally closed, even if an Exception is raised. Your code will (mostly) work without it, but it's a good habit to get into to always use ``with`` to open a file.

File Writing
------------

.. code-block:: python

    outfile = open("output.txt", "w")
    for i in range(10):
        outfile.write(f"this is line: {i}\n")
    outfile.close()

    with open("output.txt", "w") as f:
        for i in range(10):
           f.write(f"this is line: {i}\n")

File Methods
------------

Commonly used file methods:

.. code-block:: python

    f.read()
    f.readline()
    f.readlines()
    f.write(str)
    f.writelines(seq)
    f.seek(offset)
    f.tell() # for binary files, mostly
    f.close()

``StringIO``
------------

A ``StringIO`` method is a "file like" object that stores the content in memory. That is, it has all the methods of a file, and behaves the same way, but never writes anything to disk.

.. code-block:: python

    In [6]: import io

    In [7]: f = io.StringIO()

    In [8]: f.write("some stuff")
    Out[8]: 10

    In [9]: f.seek(0)
    Out[9]: 0

    In [10]: f.read()
    Out[10]: 'some stuff'

    In [11]: f.getvalue()
    Out[11]: 'some stuff'

    In [12]: f.close()

This can be handy for testing file handling code.

Paths and Directories
=====================

Paths
-----

Paths are generally handled with simple strings.

Relative paths:

.. code-block:: python

    "secret.txt"
    "./secret.txt"

Absolute paths:

.. code-block:: python

    "/home/chris/secret.txt"


Either works with ``open()``, etc.

Relative paths are relative to the current working directory, which is only relevant to command-line programs.

``os`` Module
-------------

.. code-block:: python

    import os

    os.getcwd()
    os.chdir(path)


``os.path`` module
------------------

.. code-block:: python

    import os.path

    os.path.split()
    os.path.splitext()
    os.path.basename()
    os.path.dirname()
    os.path.join()
    os.path.abspath()
    os.path.relpath()


These are all platform independent and will work the same on Windows, Linux, and macOS.

Directories
-----------

.. code-block:: python

    import os

    os.listdir()
    os.mkdir()
    os.walk()

Note the ``shutil`` module provides higher level operations and might be more useful in many situations.

pathlib
-------

``pathlib`` is a package for handling paths in an object oriented way: http://pathlib.readthedocs.org/en/pep428/

It has all the stuff in ``os.path`` and more:

.. code-block:: ipython

    In [14]: import pathlib

    In [15]: pth = pathlib.Path('./')

    In [16]: pth.is_dir()
    Out[16]: True

    In [17]: pth.absolute()
    Out[17]: PosixPath('/Users/Chris/PythonStuff/UWPCE/Fall2018-PY210A/examples/Session02')

    In [18]: for f in pth.iterdir():
        ...:     print(f)
        ...:
        ...:

And it has a really nifty way to join paths, by overloading the "division" operator:

.. code-block:: ipython

    In [49]: p = pathlib.Path.home()  # create a path to the user home dir.

    In [50]: p
    Out[50]: PosixPath('/Users/Chris')

    In [51]: p / "a_dir" / "one_more" / "a_filename"
    Out[51]: PosixPath('/Users/Chris/a_dir/one_more/a_filename')

Kinda slick, eh? This makes your code platform agnostic so that you're using the correct path separators no matter what platform you are using.

For the full docs: https://docs.python.org/3/library/pathlib.html

The Path Protocol
-----------------

As of Python 3.6, there is now a protocol for making arbitrary objects act like paths:

Read about it in PEP 519: https://www.python.org/dev/peps/pep-0519/

This was added because most built-in file handling modules, as well as any number of third party packages that needed a path, worked only with string paths.

Even after ``pathlib`` was added to the standard library, you couldn't pass a ``Path`` object in where a path was needed -- even the most common ones like ``open()``.

So you could use the nifty path manipulation stuff, but still needed to call ``str`` on it:

.. code-block:: python

    p = pathlib.Path.home() / a_filename.txt

    f = open(str(p), 'r')

Rather than add explicit support for ``Path`` objects, a new protocol was defined, and most of the standard library was updated to support the new protocol.

This way, third party path libraries could be used with the standard library as well.

What This Means to You
----------------------

Unless you are writing a path manipulation library, or a library that deals with paths other than with the stdlib packages (like ``open()``), all you need to know is that you can use ``Path`` objects most places you need a path.

Some Additional Notes
=====================

Using Files and "with"
-----------------------

Sorry for the confusion, but I'll be more clear now.

When working with files, unless you have a good reason not to, use ``with``:

.. code-block:: python

  with open(the_filename, "w") as outfile:
      outfile.write(something)
      do_some_more())

  # now done with out file -- it will be closed, regardless of errors, etc.
  do_other_stuff()

``with`` invokes a context manager -- which can be confusing, but for now, just follow this pattern -- it really is more robust.

And you can even do two at once:

.. code-block:: python

    with open(source, "rb") as infile, open(dest, "wb") as outfile:
        outfile.write(infile.read())

Binary files
------------

Python can open files in one of two modes:

* Text
* Binary

This is just what you'd think -- if the file contains text, you want text mode. If the file contains arbitrary binary data, you want binary mode.

All data in all files is binary -- that's how computers work. So in Python, "text" actually means Unicode -- which is a particular system for matching characters to binary data.

But this too is complicated -- there are multiple ways that binary data can be mapped to Unicode text, known as "encodings". In Python, text files are by default opened with the "utf-8" encoding. These days, that mostly "just works".

But if you read a binary file as text, then Python will try to interpret the bytes as utf-8 encoded text -- and this will likely fail:

.. code-block:: ipython

    In [13]: open("a_photo.jpg").read()
    ---------------------------------------------------------------------------
    UnicodeDecodeError                        Traceback (most recent call last)
    <ipython-input-13-5c699bc20e80> in <module>()
    ----> 1 open("PassportPhoto.JPG").read()

    /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/codecs.py in decode(self, input, final)
        319         # decode input (taking the buffer into account)
        320         data = self.buffer + input
    --> 321         (result, consumed) = self._buffer_decode(data, self.errors, final)
        322         # keep undecoded input until the next call
        323         self.buffer = data[consumed:]

    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte


**NOTE:** If you want to actually DO anything with a binary file, other than passing it around, then you'll need to know a lot about how the details of what the bytes in the file mean -- and most likely, you'll use a library for that -- like an image processing library for the jpeg example above.
