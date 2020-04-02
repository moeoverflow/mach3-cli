# Mach3_Cli

Recursively parse and index subtitle text for future use.

A fun project for anime fans.

[PyPI: mach3](https://pypi.org/project/mach3/)

![usage](https://raw.githubusercontent.com/Calvin-Xu/mach3-cli/master/usage.gif)


### Installation

    $ pip3 install mach3_cli
    
Or clone the project and run:

    $ pip3 install .

### Usage

```
$ mach3 [option] <argument>

options:
[-i --index] : Index subtitles in the directory
[-s --search] : Search for lines from an index database in the current directory
                Note: The database has to be in the current directory!

argument:

When indexing: the directory to index
When searching: the search query
```
    
### What it does:

Ever wanted to find a specific anime quote? Mach3 indexes your subtitle files, makes individual lines searchable & can even open the video at that line!

* Recursively finds all .ass files in the directory given.
* Parses the .ass files, regex-process the text
* Stores the text in a SQLite database
    * Silently converts encoding to UTF-8 without changing the original subtitle files
* (When searching) Queries from the SQLite database
* Opens the mpv player at the line you specify

### Open-source libraries used:

* SQLAlchemy

  * <http://sqlalchemy.org>

* python-ass: A library for parsing and manipulating Advanced SubStation Alpha subtitle files.

  * https://github.com/chireiden/python-ass
