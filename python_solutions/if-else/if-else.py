import math
import os
import random
import re
import sys

def main(n):

    if n == 3:
        print('Weird')
    elif n == 5:
        print('Weird')
    elif n > 1 and n < 6:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n > 20 and n <= 28:
        print('Not Weird')
    elif n > 28 and n < 100:
        print('Weird')
    elif n >= 100:
        print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    main(n)