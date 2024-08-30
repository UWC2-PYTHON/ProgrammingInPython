.. _sublime_as_ide:

**************************************************
Turning Sublime Text Into a Lightweight Python IDE
**************************************************

A solid text editor is a developer's best friend. You use it constantly and it becomes like a second pair of hands. The keyboard commands you use daily become so ingrained in your muscle memory that you stop thinking about them entirely.

With Sublime Text, it's possible to turn your text editor into the functional equivalent of a Python IDE. The best part is you don't have to install an IDE to do it.

http://www.sublimetext.com/

Requirements
============

Here are *my* requirements for an 'IDE':

* It should provide excellent, configurable syntax colorization.
* It should allow for robust tab completion.
* It should perform automatic code linting to help avoid silly mistakes and conform to good style.

And some more advanced features that you may want later:

* It should offer the ability to jump to the definition of symbols in other files.
* It should be able to interact with a Python interpreter such that when debugging, the editor will follow along with the debugger.

Which Version?
==============

Use version 3 -- it is updated now and again, so make sure to get the latest.

*Use Sublime Version 3*

Basic Settings
==============

All configuration in Sublime Text is done via `JSON <http://www.json.org>`_. It's simple to learn. Go and read that link then return here.

.. note:: JSON is very similar to Python dict and list literals. Though it has its root in Javascript, it is also used in a wide variety of applications,  and is well supported by Python. But a key difference is that it does not allow trailing commas after items in lists -- so be careful.

There are a number of `different levels of configuration <http://www.sublimetext.com/docs/3/settings.html>`_ in Sublime Text. You will most often work on settings at the user level.

Open ``Preferences`` -> ``Settings``

On a Mac, you can find it under:

``Sublime Text`` -> ``Preferences`` -> ``Settings``

Sublime will open up a split window -- "default" and "user" -- you can look through the default ones to see all the setting you might want to override, and then copy things from default by putting them in the user file.

The preferences file is simply a JSON text file you edit like any other text file.

Here's a reasonable set of preliminary settings (theme, color scheme and font are quite personal, find ones that suit you.):

.. code-block:: json

    {
        "auto_indent": true,
        "draw_white_space": "all",
        "font_face": "inconsolata",
        "font_size": 23,
        "indent_to_bracket": true,
        "rulers":
        [
            79,
            120
        ],
        "theme": "Adaptive.sublime-theme",
        "smart_indent": true,
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "use_tab_stops": true,
        "trailing_spaces_modified_lines_only": true,
        "trim_automatic_white_space": true,
        "trim_trailing_white_space_on_save": true,
        "word_wrap": false,
        "wrap_width": 120
    }

**NOTE:** Especially important is the setting ``translate_tabs_to_spaces``, which ensures that any time you hit a tab key, the single <tab> character is replaced by four <space> characters. In Python this is **vital**!

If you do nothing else, add ``translate_tabs_to_spaces`` to your config!

White Space Management
----------------------

One of the issues highlighted by code linters is trailing spaces. Sublime Text provides a setting that allows you to remove them every time you save a file:

.. code-block:: json

    {
        "trim_trailing_whitespace_on_save": true
    }

This is a useful setting, but be careful if you are working with existing code: removing trailing whitespace by default causes a *ton* of noise in git commits.

But if you use it from the start with your code, it will keep it clean from the beginning.

It is suggested in the above settings.
