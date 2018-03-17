# Mach3_Cli

Recursively parse and index subtitle text for future use.


### Installation

(From PyPI:) Just run:

    $ pip3 install mach3_cli
    
Or clone the project and run:

    $ pip3 install .

### Usage

To use it:

    $ mach3 --help
    
### What it does:

* Recursively find all .ass files in the directory given.
* Parse the .ass files, regex-process the text
* Store the text in a SQLite database
* (When searching) Query from the SQLite database

A fun project for anime fans.

### Open-source code used:

* SQLAlchemy

* * <http://sqlalchemy.org>

* python-ass: A library for parsing and manipulating Advanced SubStation Alpha subtitle files.

  * https://github.com/rfw/python-ass
