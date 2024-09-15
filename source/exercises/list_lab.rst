.. _exercise_list_lab:

########
List Lab
########

Goal
====

Learn the basic ins and outs of Python lists.

Hint
====

To query the user for info at the command line, you use:

.. code-block:: python

    response = input("a prompt for the user > ")

``response`` will be a string of whatever the user types (until a <return>).

Tasks
=====

In the GitHub Classroom repository for this exercise you will find a``list_lab.py`` file. If it not there, you can create it and add it to git yourself.

Make sure the file is added to your clone of the repository and commit changes frequently while working on the following tasks. When you are done, push your changes to GitHub and issue a pull request to let the instructors know it is ready for review.

When the script is run, it should accomplish the following four series of actions:

Series 1
--------

- Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
- Display the list. Plain old ``print()`` is fine.
- Ask the user for another fruit and add it to the end of the list.
- Display the list.
- Ask the user for a number and display the number back to the user and the fruit corresponding to that number, using 1 as the first number. Remember that Python uses zero-based indexing, so you will need to correct for that.
- Add another fruit to the beginning of the list using "+" and display the list.
- Add another fruit to the beginning of the list using ``insert()`` and display the list.
- Display all the fruits that begin with "P", using a for loop.

Series 2
--------

Using the list created in series 1 above:

- Display the list.
- Remove the last fruit from the list.
- Display the list.
- Ask the user for a fruit to delete, find it and delete it.
- Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.

Series 3
--------

Again, using the list from series 1:

- Ask the user for input displaying a line like "Do you like apples?" for each fruit in the list, making the fruit all lowercase.
- For each "no", delete that fruit from the list.
- For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here)
- Display the list.

Series 4
--------

Once more, using the list from series 1:

- Make a new list with the contents of the original, but with all the letters in each item reversed.
- Delete the last item of the original list. Display the original list and the copy.

This assignment was inspired by: http://www.upriss.org.uk/python/session5.html
