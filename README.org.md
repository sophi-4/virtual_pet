-*- mode: org; mode: visual-line; -*-
#+STARTUP: indent

* VIRTUAL PET
** LOCAL SETUP (macOS)
*** Install =mongodb=

Using Homebrew:

#+BEGIN_SRC shell
  brew install mongodb
#+END_SRC

*** Run local database server

Spin the database up in a terminal window:

#+BEGIN_SRC shell
  mongod --config /usr/local/etc/mongod.conf
#+END_SRC

Type =^C= to shut down. Database files are stored in =/usr/local/var/mongodb=.

*** Create a test database

Download Robo 3T: https://robomongo.org/download - this can be used for queries in the native syntax (which is similar to the =pymongo= syntax), but also just for examining data interactively.

*** Set up python virtual environment

Packages needed:

- =Flask=
- =pymongo=

*** Try a test script

In the virtual environment, run =scripts/insert.py=: this is a simple Python script for inserting some test records and printing them out.
