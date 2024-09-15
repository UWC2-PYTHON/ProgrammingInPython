.. _exercise_dict_lab:

######################
Dictionary and Set Lab
######################

Goal
====

Learn the basic ins and outs of Python dictionaries and sets.

Tasks
=====

Create a new ``dict_lab.py`` file.

Add the file to your clone of the repository and commit changes frequently while working on the following tasks.

When the script is run, it should accomplish the following four series of actions.

Part 1
------

* Create a dictionary containing "name", "city", and "cake" for "Chris" from "Seattle" who likes "Chocolate". So the keys should be: "name", etc, and values: "Chris", etc.

* Display the dictionary.

* Delete the entry for "cake".

* Display the dictionary.

* Add an entry for "fruit" with "Mango" and display the dictionary.

    - Display the dictionary keys.
    - Display the dictionary values.
    - Display whether or not "cake" is a key in the dictionary (i.e. False) (now).
    - Display whether or not "Mango" is a value in the dictionary (i.e. True).

Part 2
------

* Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 't's in each value as the value (consider upper and lower case?).

  The result should look something like::

      {
          "name": 0,
          "city": 2,
          "cake": 2,
      }

Part 3
------

* Create sets ``s2``, ``s3`` and ``s4`` that contain numbers from zero through twenty, divisible by 2, 3 and 4. Figure out a way to compute those -- don't just type them in.

* Display the sets.

* Display if s3 is a subset of s2 (False)

* Display if s4 is a subset of s2 (True)

Part 4
------

* Create a set with the letters in 'Python' and add 'i' to the set.

* Create a frozenset with the letters in 'marathon'.

* Display the union and intersection of the two sets.
