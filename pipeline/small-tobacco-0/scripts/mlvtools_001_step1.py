#!/usr/bin/env python3
# Generated from ./common/notebooks/001_step1.ipynb
from typing import List
import argparse


def mlvtools_001_step1(ifile: str, ofile: str):
    """
    :param str ifile:
    :param str ofile:
    
    :dvc-in ifile: {{ conf.intermediate }}
    :dvc-out ofile: {{ conf.model }}
    """

    with open(ofile, "w") as f:
        f.write("aggregated model\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command for script mlvtools_001_step1')

    parser.add_argument('--ifile', type=str, required=True, help="")

    parser.add_argument('--ofile', type=str, required=True, help="")

    args = parser.parse_args()

    mlvtools_001_step1(args.ifile, args.ofile)
