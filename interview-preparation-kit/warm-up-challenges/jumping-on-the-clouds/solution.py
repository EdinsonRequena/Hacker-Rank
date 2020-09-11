#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, n):
    emma, salto, n = 0, 0, n -1

    while emma < n:
        if emma + 2 <= n and c[emma + 2] == 0:
            emma += 2
            salto += 1
        elif c[emma + 1] == 0:
            emma += 1
            salto += 1
    return salto


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
