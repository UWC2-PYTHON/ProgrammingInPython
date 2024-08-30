.. _unicode:

=================
Unicode in Python
=================

A quick run-down of Unicode, its use in Python 3, and some of the gotchas that arise.

History
=======

Here is a bit about where all this mess came from.

What the heck is Unicode anyway?
---------------------------------

* First there was chaos...
  * Different machines used different encodings -- different ways of mapping the binary data that the computer stores to letters.
* Then there was ASCII -- and all was good (7 bit), 127 characters
  * (for English speakers, anyway)
* But each vendor used the top half of 8bit bytes (127-255) for different things.
  * MacRoman, Windows 1252, etc...
  * There is now "latin-1", a 1-byte encoding suitable for European languages -- but still a lot of old files around that use the old ones.
* Non-Western European languages required totally incompatible 1-byte encodings
* This means there was no way to mix languages with different alphabets in the same document (web page, etc.)

Enter Unicode
--------------

The Unicode idea is pretty simple:
  * One "code point" for all characters in all languages

But how do you express that in bytes?
  * Early days: we can fit all the code points in a two byte integer (65536 characters)
  * Turns out that didn't work -- 65536 is not enough for all languages. So we now need 32 bit integer to hold all of Unicode "raw" (UTC-4).
  * But it's a waste of space to use 4 full bytes for each character, when so many don't require that much space.

Enter "encodings":
  * An encoding is a way to map specific bytes to a code point.
  * Each code point can be represented by one or more bytes.
  * Each encoding is different -- if you don't know the encoding, you don't know how to interpret the bytes! (though maybe you can guess)

Unicode
-------

A good start: `The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!) <http://www.joelonsoftware.com/articles/Unicode.html>`_

**Everything is Bytes**

* If it's on disk or on a network, it's bytes
* Python provides some abstractions to make it easier to deal with bytes

**Unicode is a Biggie**

Actually, dealing with numbers rather than bytes is big -- but we take that for granted.

Mechanics
=========

What are strings?
-----------------

In Python 3 strings are sequences of "platonic characters".

It's almost one code point per character. There are complications with combined characters: accents, etc -- but we can mostly ignore those -- you will get far thinking of a code point as a character.

Platonic characters cannot be written to disk or network.

(ANSI: one character == one byte -- it was so easy!)

Strings vs Unicode
------------------

Python 3 is very clear:

  ``str`` for text
  ``bytes`` for binary data

Unicode
--------

The Python 3 string object lets you work with characters, instead of bytes. It has all the methods you'd expect a string object to have.

Encoding / Decoding
-------------------

If you need to deal with the actual bytes for some reason, you may need to convert between a string object and a particular set of bytes.

**"encoding"** is converting from a string object to bytes

**"decoding"** is converting from bytes to a string object

(Sometimes this feels backwards.)

As an ordinary user (particularly one that used English...), you may not notice any difference between strings and bytes -- text is text, and things generally "just work", but under the hood it is very different, and folks writing libraries for things like Internet protocols have struggled with the differences.

Encodings
----------

What encoding should I use???

There are a lot:

http://en.wikipedia.org/wiki/Comparison_of_Unicode_encodings

But only a couple you are likely to need:

* utf-8  (``*nix``)
* utf-16  (Windows)

and of course, still the one-bytes ones.

* ASCII
* Latin-1

UTF-8
-----

Probably the one you'll use most -- most common in Internet protocols (xml, JSON, etc.)

Nice properties:

* ASCII compatible: First 127 characters are the same as ASCII

* Any ascii string is a utf-8 string

* Compact for mostly-English text.

Gotchas:

* "higher" code points may use more than one byte: up to 4 for one character

* ASCII compatible means it may work with default encoding in tests -- but then blow up with real data

UTF-16
------

Kind of like UTF-8, except it uses at least 16 bits (2 bytes) for each character: NOT ASCII compatible.

But it still needs more than two bytes for some code points, so you still can't simply process it as two bytes per character.

In C/C++, it is held in a "wide char" or "wide string".

MS Windows uses UTF-16, as does (I think) Java.

UTF-16 criticism
-----------------

There is a lot of criticism on the net about UTF-16 -- it's kind of the worst of both worlds:

* You can't assume every character is the same number of bytes
* It takes up more memory than UTF-8

`UTF-16 Considered Harmful <http://programmers.stackexchange.com/questions/102205/should-utf-16-be-considered-harmful>`_

But to be fair, in early versions of Unicode, everything fit into two bytes (65536 code points). Microsoft and Java were fairly early adopters, and it seemed simple enough to just use 2 bytes per character.

When it turned out that 4 bytes were really needed, they were kind of stuck in the middle.

Latin-1
-------

**NOT Unicode**

A 1-byte per char encoding.

* Superset of ASCII suitable for Western European languages
* The most common one-byte per char encoding for European text
* Nice property -- every byte value from 1 to 255 is a valid character (at least in Python)
* You will never get an UnicodeDecodeError if you try to decode arbitrary bytes with latin-1
* And it can "round-trip" through a unicode object
* Useful if you don't know the encoding -- at least it won't raise an Exception
* Useful if you need to work with combined text+binary data

Unicode Docs
------------

Python Docs Unicode How-to: http://docs.python.org/howto/unicode.html

"Reading Unicode from a file is therefore simple"

Just use plain old open:

.. code-block:: python

    open('unicode.rst', encoding='utf-8')
    for line in f:
        print repr(line)

Encodings built-in to Python: http://docs.python.org/3/library/codecs.html#standard-encodings

Unicode in Python 3
-------------------

The "string" object **is** Unicode (always).

Python 3 has two distinct concepts:

* "text" -- uses the str object (which is always Unicode!)
* "binary data" -- uses bytes or bytearray

Everything that's about text is Unicode.

Everything that requires binary data uses bytes.

It's all much cleaner.

So you can pretty much ignore encodings and all that for most basic text processing. If you do find yourself needing to deal with binary data, you may need to encode/decode stuff yourself. In which case, Python provides an ``.encode()`` method on strings that encode the string to a bytes object with the encoding you select:

.. code-block:: ipython

    In [3]: this_in_utf16 = "this".encode('utf-16')

    In [4]: this_in_utf16
    Out[4]: b'\xff\xfet\x00h\x00i\x00s\x00'

And bytes objects have a ``.decode`` method that decodes the bytes and makes a string object:

    In [5]: this_in_utf16.decode('utf-16')
    Out[5]: 'this'

It's all quite simple an robust.

Exercises
=========

Basic Unicode LAB
-----------------

* Find some nifty non-ascii characters you might use.

  - Create a unicode object with them in two different ways.
  - :download:`here  <../examples/unicode/hello_unicode.py>` is one example

* Read the contents into unicode objects:

 - :download:`ICanEatGlass.utf8.txt <../examples/unicode/ICanEatGlass.utf8.txt>`
 - :download:`ICanEatGlass.utf16.txt <../examples/unicode/ICanEatGlass.utf16.txt>`

and / or

 - :download:`text.utf8 <../examples/unicode/text.utf8>`
 - :download:`text.utf16 <../examples/unicode/text.utf16>`
 - :download:`text.utf32 <../examples/unicode/text.utf32>`

* Write some of the text from the first exercise to file -- then read that file back in.

Some Help
---------

Reference: http://inamidst.com/stuff/unidata/

NOTE: If your terminal does not support unicode -- you'll get an error trying to print. Try a different terminal or IDE, if possible.
