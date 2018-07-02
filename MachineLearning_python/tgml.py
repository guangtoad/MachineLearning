# coding:utf-8
from tgtensorflow.tgtensorflow import tgtensorflow
import parser
import argparse
import sys
FLAGS = None
def main():
    print("hello word")
    # tgt = tgtensorflow()
    # tgt.getmnist()
    # tgt.getmnist()
    # print(tgt.name)
    pass
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--testing_percentage',
        type=int,
        default=10,
        help='What percentage of images to use as a test set.'
        )
    FLAGS, unparsed = parser.parse_known_args()
    main()