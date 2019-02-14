# -*- coding: utf-8 -*-
import argparse

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Add parser for the "create" command
    create_parser = subparsers.add_parser('create', help="Create a new project")
    create_parser.add_argument('giturl', help='url of the git repo')
    # Add parsers for the "workon" command
    workon_parser = subparsers.add_parser('workon', help="Activate a project")

    args = parser.parse_args()
    print(args)