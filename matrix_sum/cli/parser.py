from __future__ import annotations
from argparse import ArgumentParser

parser = ArgumentParser("matrix-sum")
parser.add_argument("-i", "--input", type=str, metavar='PATH', default="f0.json", help="path to input file")
parser.add_argument("-o", "--output", type=str, metavar='PATH', default="f1.json", help="path to output file")
