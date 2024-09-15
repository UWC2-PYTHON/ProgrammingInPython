#!/usr/bin/env python

"""
here is a simple main() module -- to demonstrate setuptools entrypoints
"""

import os
import sys
import capital_mod


help = """
capitalize script

capitalize file_to_process [output_file_name]

capitalizes (title case) each line in a passed in file
"""


def main():
    """
    startup function for running a capitalize as a script
    """
    try:
        infilename = sys.argv[1]
    except IndexError:
        print("you need to pass in a file name to process")
        print(help)
        sys.exit()
    try:
        outfilename = sys.argv[2]
    except IndexError:
        root, ext = os.path.splitext(infilename)
        outfilename = f"{root}_cap{ext}"

    # do the real work:
    print(f"Capitalizing: {infilename} and storing it in {outfilename}")

    capital_mod.capitalize(infilename, outfilename)

    print("I'm done")
