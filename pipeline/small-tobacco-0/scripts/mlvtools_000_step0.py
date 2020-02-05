#!/usr/bin/env python3
# Generated from ./small-tobacco-0/notebooks/000_step0.ipynb
from typing import List
import argparse


def mlvtools_000_step0(ifile: str, ofile: str):
    """
    :param str ifile:
    :param str ofile:
    
    :dvc-in ifile: {{ conf.extract }}
    :dvc-out ofile: {{ conf.intermediate }}
    """

    with open(ofile, "w") as f:
        f.write("intermediate\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command for script mlvtools_000_step0')

    parser.add_argument('--ifile', type=str, required=True, help="")

    parser.add_argument('--ofile', type=str, required=True, help="")

    args = parser.parse_args()

    mlvtools_000_step0(args.ifile, args.ofile)
