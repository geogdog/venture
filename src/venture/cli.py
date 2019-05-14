# -*- coding: utf-8 -*-
import argparse
import logging
import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from pprint import pprint

from .completion import completion
from venture import __version__

# Log config
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# Basic defaults
VENTURE_DIR = os.path.expanduser('~/.venture')
# VENTURE_CONFIG = os.path.join(VENTURE_DIR, 'venture.yml')
VENTURE_CONFIG = 'venture.yml'
WORKSPACE = os.environ.get("WORKSPACE", VENTURE_DIR)

CONFIG = {'venture': {
            'config_dir': VENTURE_DIR,
            'config_file': VENTURE_CONFIG,
            },
          'workspaces': []
         }

CONFIG['workspaces'].append({'name': 'Venture', 'vcs_url': 'git@github.com:geogdog/venture.git'})

def setup():
    # Create config dir
    logger.debug("Testing for existence of config dir: %s", VENTURE_DIR)
    if os.path.isdir(VENTURE_DIR):
        logger.debug("Config dir exists: %s", VENTURE_DIR)
    else:
        logger.debug("Creating config dir: %s", VENTURE_DIR)
        os.mkdir(VENTURE_DIR)
    # Crete config file


def read_config():
    if os.path.isfile(VENTURE_CONFIG):
        logger.debug("Read config from file")
    else:
        logger.debug("Create config file")


def main():
    parser = argparse.ArgumentParser(prog="venture")

    # Standard options
    parser.add_argument(
        '--setup', action="store_const", const=setup,
        help="setup venture"
    )
    parser.add_argument(
        '--completion', '-c', action="store_const", const=completion,
        help="print completion to stdout")

    parser.add_argument('--version', action='version', version=__version__)

    subparsers = parser.add_subparsers()

    # Add parser for the "create" command
    create_parser = subparsers.add_parser(
        'create', help="Create a new project")
    create_parser.add_argument('giturl', help='url of the git repo')
    # Add parsers for the "workon" command
    workon_parser = subparsers.add_parser('workon', help="Activate a project")
    workon_parser.add_argument('projct', help='The name of the project')

    args = parser.parse_args()

    if args.completion:
        args.completion()
    if args.setup:
        args.setup()

    read_config()

    print(dump(CONFIG, default_flow_style=False, Dumper=Dumper, explicit_start=True, explicit_end=True))
