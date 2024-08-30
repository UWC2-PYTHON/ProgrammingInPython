.. _dict_as_switch:

################################
Using a Dictionary to ``switch``
################################

Until Python 3.10, there was no switch/case statement available in Python. It had been `proposed but rejected <https://peps.python.org/pep-3103/>`_ until finally `it was accepted <https://peps.python.org/pep-0636/>`_ and called match/case. But there is a pattern that you will run across often that uses dicts to act like a switch.

``switch`` / ``case``
=====================

What is ``switch``/``case`` and ``match``/``case``?
---------------------------------------------------

Many languages have a "switch-case" construct::

    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };

How do you say this in Python?

``if-elif`` chains
------------------

The obvious way to say it is a chain of ``elif`` statements:

.. code-block:: python

    if argument ==  0:
        return "zero"
    elif argument == 1:
        return "one"
    elif argument == 2:
        return "two"
    else:
        return "nothing"

And there is nothing wrong with that, but it's very ugly and hard to read.

Or, if you are using at least Python 3.10, you can use ``match/case`` statements:

.. code-block:: python

    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case _:
            return "nothing"

And you can use that, too, but the indenting gets to be a bit much for doing anything non-trivial.

``dict`` as ``switch``
----------------------

The ``elif`` chain is neither elegant nor efficient. The ``match/case`` block works very well but can get hard to read quicklky. There are a number of ways to say it in python -- but one elegant one is to use a dict:

.. code-block:: python

    arg_dict = {
        0: "zero",
        1: "one",
        2: "two",
    }
    arg_dict.get(argument, "nothing")

Simple, elegant and fast.

You can do a dispatch table by putting functions as the value.

Switch with Functions
---------------------

What would this be like if you used functions instead? Think of the possibilities.

.. code-block:: python

    def my_zero_func():
        return "I'm zero"

    def my_one_func():
        return "I'm one"

    switch_func_dict = {
        0: my_zero_func,
        1: my_one_func,
    }

    switch_func_dict.get(0)()

Again, fast and efficient.

This is possible because functions are "first class objects" in Python.

This will come in handy on your assignments when trying to implement a menu system. Rather than writing a whole series of if/elif statements you can call into a dict with the user's menu choice.
