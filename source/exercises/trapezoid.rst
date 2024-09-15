.. _exercise_trapezoidal_rule:

################
Trapezoidal Rule
################

Goal:

    Making use of functions as objects -- functions that act on functions.

Trapezoidal rule
----------------

The "trapezoidal rule": https://en.wikipedia.org/wiki/Trapezoidal_rule

It is one of the easiest "quadrature" methods, otherwise known as computing a definite integral, or, simply: computing the area under a curve.

The Task
--------

Your task is to write a ``trapz()`` function that will compute the area under an arbitrary function using the trapezoidal rule.

The function will take another function as an argument, as well as the start and end points to compute, and return the area under the curve.

Example
-------

.. code-block:: python

    def line(x):
        '''a very simple straight horizontal line at y = 5'''
        return 5

    area = trapz(line, 0, 10)

    area
    50

About the simplest "curve" you can have is a horizontal straight line, in this case, at y = 5. The area under that line from 0 to 10 is a rectangle that is 10 wide and 5 high, so with an area of 50.

Of course in this case, it's easiest to simply multiply the height times the width, but we want a function that will work for **any** curve.

Hint: this simple example could be a good test case!

The Solution
------------

Your function definition should look like:

.. code-block:: python

    def trapz(fun, a, b):
        """
        Compute the area under the curve defined by
        y = fun(x), for x between a and b

        :param fun: the function to evaluate
        :type fun: a function that takes a single parameter

        :param a: the start point for the integration
        :type a: a numeric value

        :param b: the end point for the integration
        :type b: a numeric value
        """
        pass


In the function, you want to compute the following equation:

.. math::

    area = \frac{b-a}{2N}(f(x_0) + 2f(x_1) + 2f(x_2) + \dotsb + 2f(x_{N-1}) + f(x_N))

So you will need to:

- create a list of x values from a to b (maybe 100 or so values to start)
- compute the function for each of those values and double them
- add them all up
- multiply by the half of the difference between a and b divided by the number of steps.

Note that the first and last values are not doubled, so it may be more efficient to rearrange it like this:

.. math::

    area = \frac{b-a}{N} \left( \frac{f(x_0) + f(x_{N})}{2} + \sum_{i=1}^{N-1} f(x_i) \right)

**Note:** For those of you confused by that weird big greek letter, see: :ref:`sum_explained`

Can you use comprehensions for this?

Remember that ``range()`` only works for integers. How can you deal with that?

Once you have that, it should work for any function that can be evaluated between a and b.

Try it for some built-in math functions like ``math.sin``.

Tests
-----

Do this using test-drive development.

A few examples of analytical solutions you can use for tests:

* A simple horizontal line -- see above.
* A sloped straight line:

.. math::

  \int_a^b  y = mx + B = \frac{1}{2} m (b^2-a^2) + B (b-a)

* The quadratic:

.. math::

  \int_a^b  y = Ax^2 + Bx + C = \frac{A}{3} (b^3-a^3) + \frac{B}{2} (b^2-a^2) + C (b-a)

* The sine function:

.. math::

  \int_a^b \sin(x) = \cos(a) - \cos(b)

Computational Accuracy
----------------------

In the case of the linear functions, the result should theoretically be exact. However, with the vagaries of floating point math, they may not be.

And for non-linear functions, the result will certainly not be exact.

So you want to check if the answer is *close* to what you expect.

In Python there is an ``isclose()`` function, as defined in PEP-485: https://www.python.org/dev/peps/pep-0485/

Stage Two
---------

Some functions need extra parameters to do their thing. But the above will only handle a single parameter. For example, a quadratic function:

.. math::

    y = A x^2 + Bx + C

This requires values for A, B, and C in order to compute y from an given x.

You could write a specialized version of this function for each A, B, and C:

.. code-block:: python

    def quad1(x):
        return 3 * x**2 + 2*x + 4

But then you need to write a new function for any value of these parameters you might need.

Instead, you can pass in A, B and C each time:

.. code-block:: python

    def quadratic(x, A=0, B=0, C=0):
        return A * x**2 + B * x + C

Nice and general purpose.

But how would we compute the area under this function?

The function we wrote above only passes x in to the function it is integrating.

Passing Arguments Through
-------------------------

Update your ``trapz()`` function so that you can give it a function that takes arbitrary extra arguments, either positional or keyword, after the x.

So you can do:

.. code-block:: python

    trapz(quadratic, 2, 20, A=1, B=3, C=2)

Or:

.. code-block:: python

    trapz(quadratic, 2, 20, 1, 3, C=2)

Or:

.. code-block:: python

    coef = {'A':1, 'B':3, 'C': 2}
    trapz(quadratic, 2, 20, **coef)


**Note:** Make sure this will work with ANY function, with **ANY** additional positional or keyword arguments and not just this particular function.

This is pretty conceptually challenging -- but it's very little code!

If you are totally lost then look at the lecture notes from previous classes. How can you both accept and pass arbitrary arguments to/from a function?

You want your trapz function to take ANY function that can take ANY arbitrary extra arguments, not just the quadratic function, and not just ``A``, ``B``, and ``C``. So good to test with another example.

The generalized sine function is:

.. math::

    A \sin(\omega t)

Where :math:`A` is the amplitude, and :math:`\omega` is the frequency of the function. In this case, the area under the curve from a to b is:

.. math::

    \frac{A}{\omega} \left( \cos(\omega a) - \cos(\omega b) \right)

The test code has a test for this one, too.

Currying
--------

Another way to solve the above problem is to use the original ``trapz``, and create a custom version of the ``quadratic()`` function instead.

Write a function that takes ``A``, ``B``, and ``C`` as arguments, and returns a function that evaluates the quadratic for those particular coefficients.

Try passing the results of this into your ``trapz()`` and see if you get the same answer.

partial
-------

Do the above with ``functools.partial`` as well.

Extra Credit
------------

This isn't really the point of the exercise, but see if you can make it dynamically accurate.

How accurate it is depends on how small the chunks are that you break the function up into.

See if you can think of a way to dynamically determine how small a step you should use.

This is one for the math and computational programming geeks!

.. _sum_explained:

A Bit About Math Symbology
--------------------------

Those of you without a lot of math background may be confused by the symbols. So here's a quick intro to the "Summation Symbol, also known as the Greek Capital sigma.

.. math::

    \sum_{i=a}^{b} x_i

This is shorthand for "add up a bunch of values, with varying i from a to b", where each x is a different value each time. Translating this into code you get:

.. code-block:: python

    x = a_list_of_numbers
    total = 0
    for i in range(a, b+1):
        total += x[i]

Or, in more compact python:

.. code-block:: python

    x = an iterable_of_numbers
    total = sum(x[a:b+1])

So the full expression used above:

.. math::

    \sum_{i=1}^{N-1} fun(x_i)

Can be written as:

.. code-block:: python

    sum(func(x) for x in list_of_x[1:-1])
