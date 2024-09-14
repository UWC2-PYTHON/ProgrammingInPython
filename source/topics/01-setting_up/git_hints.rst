.. _git_hints:

#########
Git Hints
#########

Git is a very complex system, and can be used in many ways. Because of this, it can be hard to find answers to seemingly simple questions, even though the Internet is full of discussions of how to use Git.

Every group using git has to establish a standard "work flow". If you search "git workflow" on the internet you find a LOT of discussion, and they are not all the same. And depending on the workflow you are using, the problems you'll have and the solutions to them will be different.

We are using a very simplified workflow with GitHub Classroom for this class, and this page seeks to provide solutions to problems that you might encounter specifically with this workflow.

.. note:: This is a page for reference. It is a bit outdated, and should not be required right off. But do remember that it's here if you get tangled up in Git as we move along.

"origin" and "upstream"
=======================

Git is a "distributed version control system". That means that git repositories are self contained, and can be "connected" with multiple other, remote repositories -- that is, repos on other machines elsewhere on the internet.

This facilitates collaboration with widely dispersed groups, but as it allows essentially arbitrary complexity, some conventions have emerged.

A git repo can be "connected" with virtually any number of remote repositories. You can see what yours is connected to with:

.. code-block:: bash

    $ git remote -v

After cloning a repository (from GitHub, for instance) on your machine, is will look something like this:

.. code-block:: bash

    $ git remote -v
    origin  https://github.com/PythonCHB/Sp2018-Accelerated.git (fetch)
    origin  https://github.com/PythonCHB/Sp2018-Accelerated.git (push)

So I have one remote repository, on GitHub. It is listed twice, as I am both fetching from (pulling) and pushing to the same repository. "origin" is created when you do a clone, and it is the one that is pushed to and pulled from by default. Git is so flexible that you could set it up to push and pull by default to two different repos, but I've never seen that done.

There is often use for having more than one remote repository, to keep various workflows in sync. But with GitHub classroom, you will have one: the "origin" remote that was created when you cloned your GitHub repo.

Adding a remote
---------------

If you do need to add a remote, you it's pretty easy:

.. code-block:: bash

    $ git remote add name_of_remote https://the_long_url_to_the_remote_repo.git

Changing a remote
-----------------

If your remotes are not set up right then you can reset them, but removing one:

.. code-block:: bash

    $ git remote remove origin

And then adding it back correctly:

.. code-block:: bash

    $ git remote add origin https://the_long_url_to_the_remote_repo.git

Working with "origin"
---------------------

If you were to try to push to the origin, it may fail if you do not have permissions to push. But when you do:

.. code-block:: bash

    $ git pull origin main

You are telling git to pull all the latest changes from the "origin" repository into your local one. Note that all of your local changes will only get into your repo on GitHub (origin) when you push:

.. code-block:: bash

    $ git push

Note that "origin" is the default remote, and "main" is the default branch, so that command is the same as:

.. code-block:: bash

    $ git pull origin main

And when you pull from your GitHub repo (``git pull``) that is shorthand for:

.. code-block:: bash

    $ git pull origin main

Note that you may not have a reason to pull from your origin repo. But if you were to work on two different machines -- say a personal laptop at home, and a work machine at the office, you could push stuff to your GitHub repo from both, and use ``git pull`` to keep your changes in sync.

In fact, I highly recommend using Git and GitHub as a way to coordinate your personal work if you have multiple machines (or multiple OSes, or...). You also get a backup essentially for free that way.

Backing out a change
====================

If you change a file in your repository and you decide that you simply want to put it back the way it was the last time you committed it -- that's easy:

.. code-block:: bash

    $ git checkout the_name_of_the_file

This only works if the change has not been committed to the repository.

Backing out a change that has been committed
--------------------------------------------

Here's the situation:

I accidentally changed a file in the examples directory in my fork of the repository.

Then I committed it, and pushed that commit to GitHub and did a PR.

So how do I back this out?

What you want to do is "checkout" the file from a previous commit.

So the first step is to find a commit that has the correct version of the file.

In this example, the file in question is:

``examples/Session05/mailroom_test.py``

I can use ``git log`` to figure out when the file was last touched:

.. code-block:: bash

    $ git log  examples/Session05/mailroom_test.py

That means: "show me the log of that particular file". ``git log`` by itself will show you the history of the entire repo -- less useful in this case.

In this case, I got:

.. code-block:: bash

    $ git log  examples/Session05/mailroom_test.py
    commit 87d27a12bcae5c1bdc565e05e954e7c94bfa27e0 (HEAD -> main, origin/main, origin/HEAD)
    Author: Chris Barker <PythonCHB@gmail.com>
    Date:   Sat Dec 9 16:18:22 2017 -0800

        adding a bit just to test...

    commit 8e5908a37d7df90263057644fef7138e77838107
    Author: Chris Barker <PythonCHB@gmail.com>
    Date:   Sun Nov 5 11:12:06 2017 -0800

        some updates

    commit 4795ddf41f20cfc4346f02319ab61699e8a469f2
    Author: Chris Barker <PythonCHB@gmail.com>
    Date:   Tue Oct 31 18:59:31 2017 -0700

        added mailroom review

The entry at the top, from Dec 9th, is the one I want to get rid of, so I want to checkout the version of the file back to the one before that top entry.

Each "commit" is essentially a snapshot of the entire repo when "git commit" was run. Each one is identified by a unique "hash" -- that long string of characters.

To restore a file back to the state in a previous commit, we can run:

.. code-block:: bash

    git checkout 8e5908a37d7d examples/Session05/mailroom_test.py

And that puts it back to the state it was in at that previous commit, identified by that "hash".

Note that the full hash for each commit is really long, but git will figure out what you meant if you use enough characters to uniquely identify the commit -- the first ten or so characters (e.g. "8e5908a37d") or so is usually plenty.

git blame
=========

``git blame`` is a handy utility for examining the history of a particular part of a particular file. For example:

``git blame -L 2,6 examples/Session05/mailroom_test.py``

That means: "show me the changes to lines 2--6 of this file".

It's called *"blame"* because you can use it to figure out who to blame for a change in a file.

Here's what I got with that example::

    4795ddf4 (Chris Barker 2017-10-31 18:59:31 -0700 2) from os import system
    4795ddf4 (Chris Barker 2017-10-31 18:59:31 -0700 3)
    87d27a12 (Chris Barker 2017-12-09 16:18:22 -0800 4) # some extra in here just to test git
    87d27a12 (Chris Barker 2017-12-09 16:18:22 -0800 5)
    4795ddf4 (Chris Barker 2017-10-31 18:59:31 -0700 6)

So this shows me that it was changed on 12-09, and before that on 10-31. In this case, I'm the only one that has messed with that file, so no one to shift the blame too :)

.. _git_branching:

Branching
=========

A really quick intro to branching.

You may want to start with this tutorial to familiarize yourself with the idea: https://www.atlassian.com/git/tutorials/using-branches

Quick Tutorial
--------------

You create a new "branch" with git with the branch command:

.. code-block:: bash

    $ git branch the_name_of_the_branch

Where ``the_name_of_the_branch`` is the name of the branch, naturally, which can be anything you want but should be descriptive. To see all the branches you have, you can simply run:

.. code-block:: bash

    $ git branch

The "current" branch or "HEAD" will be marked with an asterisk.

To switch to another branch, you can checkout the branch:

.. code-block:: bash

    $ git checkout the_name_of_the_branch

You are now working in the new branch. Anything you commit will be committed to that branch, and no longer effect the main branch.

If you do a ``git push`` -- you will get a message from git telling you that the branch you are now on is not set up to push to "origin" (your GitHub repo), but it will show you the command you need to set that up -- set-upstream:

.. code-block:: bash

  $ git push --set-upstream origin the_name_of_the_branch

Now it will push to GitHub, and you can see it there.

You can create Pull Requests from that new branch, as well as the old, main, branch.

Merging
-------

When you are happy with your work in the new branch, you may want to merge it back into the "main" branch.

Yu can do this by switching to the main branch:

.. code-block:: bash

    $ git checkout main

And then merging your new work into it:

.. code-block:: bash

    $ git merge the_name_of_the_branch

And there you go!

There is a saying in the git world:

    "Branch early, merge often"

It's a good way to work -- branching and merging is easy enough it git that it pays off to do it often.

"detached HEAD"
---------------

Above, we talked about using ``git checkout`` to restore a file to the state it was in in a previous commit, like so:

.. code-block:: bash

    $ git checkout 8e5908a37d7d examples/Session05/mailroom_test.py

But what happens if you do a checkout with a commit, and no specific file?

It does what you might expect -- puts ALL the files back the way they were at that commit. But there is a hitch ... let's see what happens when I do that:

.. code-block:: bash

    $ git checkout c03bb5b2c401c
    Note: checking out 'c03bb5b2c401c'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -b with the checkout command again. Example:

      git checkout -b <new-branch-name>

    HEAD is now at c03bb5b adding print_grid from class

So the files are set to the old state -- but now there is that note about "detached HEAD" -- this means that changes you make, even commits, will not effect the git repo. If you want to start from here and make changes that will stick, you need to do what it says, and make a new branch. But what it DOESN'T tell you is how to simply "re-attach" the HEAD. Turns out there is an easy way:

.. code-block:: bash

    $ git checkout -
    Previous HEAD position was c03bb5b adding print_grid from class
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.

The dash means "the branch or commit you were on before your last checkout command".

For more info about "detached HEAD", see:

https://www.cloudbees.com/blog/git-detached-head
