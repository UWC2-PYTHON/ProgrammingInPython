.. _nosql:

################
No SQL Databases
################

"No SQL"?
=========

Structured Query Language (SQL) is the standard language for communicating with relational database management systems (RDBMS).

But an RDBMS system is not always the best way to store your data.

There are other alternatives, each with there own approach, but as RDBMSs and SQL are so ubiquitous, they are all lumped in under the moniker "NoSQL".

I personally hate things that are defined by what they are NOT, rather than what they are, but that's the terminology these days.

What is a Database?
-------------------

A database is an organized collection of data. The data are typically organized to model relevant aspects of reality in a way that supports processes requiring this information.

Usually a way to persist and recover that organized data.

These days, when you say "Database" almost everyone thinks "Relational Database", and SQL is the standard way to do that.

SQL RDBMS systems are robust, powerful, scalable, and very well optimized.

But: they require you to adapt the relational data model.

Non-RDBMS Options
-----------------

A key buzzword these days is "NOSQL".

OK: They don't use SQL -- but what are they?

NoSQL databases are not just one thing, but they are about key features that are mostly shared:

* "schema less"

    - Document oriented

* More direct mapping to an object model
* Highly Scalable

    - Easier to distribute / parallelize than RDBMSs

Database Schema
---------------

A database schema is the organization of data, and description of how a database is constructed. It is divided into tables and relationships -- foreign keys, etc.

It includes what fields are in which tables, what data type each field is, normalization of shared data, etc.

This requires a fair bit of work up-front, and can be hard to adapt as the system requirements changes.

It also can be a bit ugly to map your programming data model to the schema.

Schema-less
-----------

Schemaless databases generally follow a "document model".

Each entry in the database is a "document":

* Essentially an arbitrary collection of fields.
* Often looks like a Python dict.

Not every entry has to have exactly the same structure.

Maps well to dynamic programming languages.

Adapts well as the system changes.

NoSQL in Python
---------------

Three Categories:

1. Simple key-value object store:
---------------------------------

- shelve
- anydbm
- can store (almost) any Python object
- only provides storage and retrieval

2. External NoSQL System
------------------------

* Python bindings to external NoSQL system
* Doesn't store full Python objects
* Generally stores arbitrary collections of data (but not classes)
* Can be simple key-value stores:

    - Redis
    - Memcached

* Or a more full featured document database:

    - In-database searching, etc.
    - MongoDB
    - AWS DocumentDB

* "Graph" databases

    - neo4j

* Or a Map/Reduce engine:

    - Hadoop

3. Python Object Database
-------------------------

* Stores and retrieves arbitrary Python objects.

    - Don't need to adapt your data model at all

* ZODB is the only robust maintained system (I know of)
* ZODB is as close a match as you can get between the store and your code -- references and everything.

Why a DB at all?
----------------

Reasons to use a database:

- You need to persist the data your application uses.
- You may need to store more data than you can hold in memory.
- You may need to have multiple applications (or multiple instances) accessing the same data.
- You may need to scale -- have the DB running on a separate server(s).
- You may need to access data from systems written in different languages.

ZODB
----

The Zope Object Data Base: A native object database for Python.

* Transparent persistence for Python objects
* Full ACID-compatible transaction support (including savepoints)
* History/undo ability
* Efficient support for binary large objects (BLOBs)
* Pluggable storages
* Scalable architecture

`ZODB <http://www.zodb.org/>`_

MongoDB
--------

Document-Oriented Storage

    * JSON-style documents with dynamic schemas offer simplicity and power.

Full Index Support

    * Index on any attribute, just like you're used to.

Replication & High Availability

    * Mirror across LANs and WANs for scale and peace of mind.

Auto-Sharding

    * Scale horizontally without compromising functionality.

Querying

    * Rich, document-based queries.

`MongoDB Web Site <https://www.mongodb.org/>`_

Other Options to Consider
-------------------------

Redis, which is an addvanced, scalable key-value store. Redis is not very well supported on Windows. It is also going through some licensing changes and alternatives like Valkey might be a better option in the future.

- http://redis.io/
- https://valkey.io/

Riak, which is a high availablity and high scalablity data store. But it's not very good for small installations.

- http://docs.basho.com/riak/latest/dev/taste-of-riak/python/

Apache Cassandra: A more schema-based NoSQL solution

- https://pypi.org/project/cassandra-driver/

This is a nice page with a summary:

- https://www.fullstackpython.com/no-sql-datastore.html

An Example
==========

The following are examples of using some of these systems to store some data.

The Data Model
--------------

To store your data, you need to have a structure for the data -- this is the data model. For this example, we will build an Address Book with a not quite trivial data model.

I'm a programmer first, and a database guy second (or third or...) so I start with the data model I want in the code.

There are people::

    self.first_name
    self.last_name
    self.middle_name
    self.cell_phone
    self.email

There are households::

    self.name
    self.people
    self.address
    self.phone


:download:`address_book_model.py <../examples/nosql/address_book_model.py>`

Using ZODB
----------

Here is an example where we will store Python objects with ZODB.

To make an object persistent you can use this syntax:

.. code-block:: python

  import persistent

  class Something(persistent.Persistent):
      def __init__(self):
          self.a_field = ""
          self.another_field = ""

When a change is made to the fields, the database will keep it updated.

Mutable Attributes
------------------

``Something.this = that`` will trigger a DB action

But:

``Something.a_list.append`` will not trigger anything.

The database doesn't know that that the list has been altered.

Here's a solution::

    from persistent.list import PersistentList

    self.a_list = PersistentList()

See also ``PersistantDict()``.

:download:`address_book_zodb.py <../examples/nosql/address_book_zodb.py>`

MongoDB
-------

MongoDB is essentially a key-value store, but the values are JSON-like objects.

So you can store any object that can look like JSON:

* dicts
* lists
* numbers
* strings
* richer than JSON.

MongoDB and Python
------------------

MongoDB is written in C++ but can be accessed by various language drivers: http://docs.mongodb.org/manual/applications/drivers/

For Python: ``PyMongo``

https://www.mongodb.com/resources/languages/pymongo-tutorial

To install the Python API for MongoDB:

    pip install pymongo

Getting Started with MongoDB
----------------------------

The MongoDB (database) is a separate program. You can find installers here:

https://www.mongodb.com/try/download/community-edition

**NOTE:** MongoDB is also available as a service, with a free "sandbox" to try it out:

https://www.mongodb.com/products/platform/atlas-database

Creating a Database
-------------------

Once you've got the database installed and you can connect to it, then make sure you've got the mongo drivers installed::

    pip install pymongo

.. code-block:: python

    # create the DB
    from pymongo import MongoClient

    client = MongoClient("localhost", 27017)
    store = client.store_name # creates a Database
    people = store.people # creates a collection

Mongo will link to the given database and collection, or create new ones if they don't exist.

Add some stuff to the collection in your database:

.. code-block:: python

    people.insert_one({'first_name': 'Fred',
                       'last_name': 'Jones'})

Pulling Stuff Out
-----------------

Here's how to read it back out:

.. code-block:: ipython

  In [16]: people.find_one({'first_name':"Fred"})
  Out[16]:
    {'_id': ObjectId('534dcdcb5c84d28b596ad15e'),
     'first_name': 'Fred',
     'last_name': 'Jones'}

Note that it adds an ObjectID for you.

:download:`../examples/nosql/address_book_mongo.py`

:download:`../examples/nosql/test_address_book_mongo.py`
