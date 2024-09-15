.. _exercise_grid_printer:

#####################
Grid Printer Exercise
#####################

Goal
====

Write a function that draws a grid like the following::

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

Hints
=====

Here are a couple features to get you started.

Printing
--------

To print more than one value on a line, you can pass multiple names into the print function:

.. code-block:: python

    print("+", "-"")

If you don't want a newline after something is printed, you can tell Python what you want the print to end with like so:

.. code-block:: python

    print("+", end=" "")
    print("-")

The output of these statements is ``'+ -'``.

The end parameter defaults to a newline.

No Arguments
------------

A print function with no arguments ends the current line and goes to the next line:

.. code-block:: python

    print()

This simply prints an empty line.

Simple String Manipulation:
---------------------------

You can put two strings together with the plus operator:

.. code-block:: ipython

    In [20]: "this" + "that"
    Out[20]: 'thisthat

This is called concatenation.

Concatenation is particularly useful if the strings have been assigned names:

.. code-block:: ipython

    In [21]: plus = '+'

    In [22]: minus = '-'

    In [23]: plus + minus + plus
    Out[23]: '+-+'

Note that you can link any number of operations together in an expression.

Multiplication of Strings
-------------------------

You can also multiply strings:

.. code-block:: ipython

    In [24]: '+' * 10
    Out[24]: '++++++++++'

And combine that with plus in a complex expression:

.. code-block:: ipython

    In [29]: first_name = 'Chris'

    In [30]: last_name = 'Barker'

    In [31]: 5 * '*' + first_name +' ' + last_name + 5 * '*'
    Out[31]: '*****Chris Barker*****'

Note that there are better ways to build up complex strings, but we'll get to that later.

Now you've got what you need to print that grid.

Give it a try!

Part 2
======

Let's make it more general. by making it a function.

One of the points of writing functions is so you can write code that does similar things, but customized by the values of input parameters. So what if we want to be able to print that grid at an arbitrary size?

Write a function ``print_grid(n)`` that takes one integer argument and prints a grid just like before, *BUT* the size of the grid is given by the argument.

For example, ``print_grid(9)`` prints the grid at the top of this page.

``print_grid(3)`` would print a smaller grid::

    + - + - +
    |   |   |
    + - + - +
    |   |   |
    + - + - +


``print_grid(15)`` prints a larger grid::

    + - - - - - - - + - - - - - - - +
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    + - - - - - - - + - - - - - - - +
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    + - - - - - - - + - - - - - - - +


This problem is under specified. Do something reasonable.

Part 3
======

Let's make it even more general by adding more parameters.

Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.

For example, ``print_grid2(3,4)`` results in::

    + - - - - + - - - - + - - - - +
    |         |         |         |
    |         |         |         |
    |         |         |         |
    |         |         |         |
    + - - - - + - - - - + - - - - +
    |         |         |         |
    |         |         |         |
    |         |         |         |
    |         |         |         |
    + - - - - + - - - - + - - - - +
    |         |         |         |
    |         |         |         |
    |         |         |         |
    |         |         |         |
    + - - - - + - - - - + - - - - +

This is three rows, three columns, and each grid cell four is "units" in size.

What to do about rounding? You decide.

Another example: ``print_grid2(5,3)``::

    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +

Have fun!

This was adapted from Downey, "Think Python", ex. 3.5
