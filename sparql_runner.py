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
import argparse


##################
# Main functions #
##################
def run(args):
    """Main functions to run."""
    input_dir = args.input_dir


def main():
    """Parse arguments and run main function."""
    parser = argparse.ArgumentParser(description="Simple program providing" +
                                     "very basic interface to SPARQL query" +
                                     "files.",
                                     prog="SPARQL runner",
                                     epilog="Konrad Zdeb @ GPL 3-0")
    parser.add_argument("-i", help="Input directory with SPARQL query" +
                        "that %(prog)s will use to run queries.",
                        dest="input_dir", type=str, required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
