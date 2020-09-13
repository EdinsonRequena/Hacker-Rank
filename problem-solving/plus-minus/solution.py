#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    natural = []
    negativo = []
    cero = []

    for i in range(0, len(arr)):
        if arr[i] > 0:
            natural.append(i)
        elif arr[i] < 0:
            negativo.append(i)
        else:
            cero.append(i)

    print(len(natural)/ len(arr))
    print(len(negativo)/ len(arr))
    print(len(cero)/ len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
