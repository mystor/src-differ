from __future__ import print_function
import os, sys
from itertools import combinations
from differ import diff

def diffdir(directory):
    files = os.listdir(directory)
    for file1, file2 in combinations(files, 2):
        file1 = os.path.join(directory, file1)
        file2 = os.path.join(directory, file2)

        try:
            print("{}, {} => {}".format(file1, file2, diff(file1, file2)))
        except:
            pass
            # print("{}, {} => Skipped".format(file1, file2))


if __name__ == '__main__':
    diffdir(sys.argv[1])
