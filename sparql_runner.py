#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Konrad <konrad.zdeb@me.com>
#
# Distributed under terms of the MIT license.

"""
This simple script provides a mechanism to run SPARQL files. The files are
sourced from within Python directory available in the package. The script reads
files as available in the provided folder and coffers convenient running
mechanism for all of the available files.
"""

###########
# Modules #
###########
import os
import argparse


#############
# Functions #
#############
def check_directory(input_dir):
    """Check if directory exists and if it's not empty."""
    if not os.path.exists(input_dir):
        print("Error: provided path does not exist.")
        os._exit(1)
    if not os.path.isdir:
        print("Error: provided path is not a directory.")
        os._exit(1)
    if not os.listdir(input_dir):
        print("Error: provided directory is empty.")
        os._exit(1)


def list_query_files(input_dir):
    """List query files from the provided directory."""
    all_files = os.listdir(input_dir)
    # Filter to match files of desired extensions only
    query_files = filter(lambda x: x[-4:] in '.txt', all_files)
    return query_files


####################
# Arguments / run  #
####################
def run(args):
    """Main functions to run."""
    input_dir = args.input_dir
    input_extensions = args.input_extensions
    check_directory(input_dir)


def main():
    """Parse arguments and run main function."""
    parser = argparse.ArgumentParser(description="Simple program providing" +
                                     "very basic interface to SPARQL query" +
                                     "files.",
                                     prog="SPARQL runner",
                                     epilog="Konrad Zdeb @ GPL 3-0")
    parser.add_argument("-i", '--input_dir', help="Input directory with SPARQL query" +
                        "that %(prog)s will use to run queries.",
                        dest='input_dir', type=str, required=True)
    parser.add_argument('-e', '--extensions', help='File extensions to use' +
                        'defaults when searching for query files.',
                        dest='input_extensions', required=False,
                        nargs='+', type=str,
                        default=['.sql', '.txt', '.sparql'])
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
