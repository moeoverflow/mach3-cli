import click
import os
from mach3.subtitle_parse import recursive_index
from mach3.db_index import add_entries
import sqlalchemy
from textwrap import dedent
from mach3.db_query import index_search
from mach3.mkv_interface import mkv_play


@click.command()
@click.option('--index', '-i', is_flag=True, help='Index anime in directory: ')
@click.option('--search', '-s', is_flag=True, help='Search for line in database:')
@click.option('--help', '-h', is_flag=True, help='Show usage:')
@click.argument('dir_query', default=os.getcwd(), required=False)
def main(index, search, help, dir_query):
    """Recursively parse, index and store subtitle text."""
    if index:
        click.echo("Recursively parsing lines at: {}".format(dir_query))
        try:
            parse_result = recursive_index(dir_query)
        except FileNotFoundError:
            click.echo("Error: No such file or directory: {}".format(dir_query))
            exit(0)
        click.echo("Parsing complete")
        click.echo("Indexing lines at: {}".format(dir_query))
        add_entries(parse_result, dir_query)
        click.echo("Indexing complete")
    elif search:
        click.echo("Searching {} from index".format(dir_query))
        try:
            options = index_search(dir_query)
        except NameError:
            click.echo("No index database found. Please index this directory first: $ mach3 -i")
            exit(0)
        if len(options) == 0:
            click.echo("I cannot find anything for you, Misaka tries and fails.")
            exit(0)
        try:
            usr_input = int(input("Choose a line: ")) - 1
            if usr_input > int(len(options)):
                usr_input = len(options) - 1
            choice = options[usr_input]
            file_name = choice["file"]
            start = choice["start"]
            end = choice["end"]
            mkv_play(file_name, start, end)
        except ValueError:
            click.echo("I cannot understand this integer, Misaka fails and is confused.")
    elif help:
        help_text = dedent("""
        ---------------------------
        $ mach3 [option] <argument>
        
        options:
        [-i --index] : Index subtitles in the directory
        [-s --search] : Search for lines from an index database in the current directory 
                        Note: The database has to be in the current directory!
                        
        argument:
        
        When indexing: the directory to index
        When searching: the search query
        ----------------------------
        """)
        click.echo(help_text)
    else:
        default_text = dedent("""
        ---------------------------
            /|    //||                                    ___    
           //|   // ||     ___      ___     / __        //   ) ) 
          // |  //  ||   //   ) ) //   ) ) //   ) )      __ / /  
         //  | //   ||  //   / / //       //   / /          ) )  
        //   |//    || ((___( ( ((____   //   / /     ((___/ / 
        
        Created with ♥ by Calvin Xu. Mar 2018
        For anime fans & more
        
        For help:
        $ mach3 -h
        ----------------------------
        """)
        click.echo(default_text)
        exit(0)
