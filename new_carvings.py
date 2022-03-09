#!/usr/bin/env python3

import argparse
import pathlib
import uuid

def main(total):
    """Creates new datafiles for carvings."""
    for data_file in range(total):
        page_id = uuid.uuid4()
        # TODO: absolute path based on file
        with open(pathlib.Path(__file__).parent.resolve() / "_carvings" / f"{page_id}.md", "w") as cf:
            cf.write("---\navailable: \ncontext: \ndate_created: \ndimensions: \nimages: \nlocations: \nmaterial: \n---")


parser = argparse.ArgumentParser(description='Add datafiles for carvings.')
parser.add_argument('total', type=int, help='the number of files to produce')
args = parser.parse_args()
main(args.total)
