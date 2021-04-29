#!/bin/python3
from statistics import median
import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    arr=[]
    for i in range(len(values)):
        while freqs[i]:
            arr.append(values[i])
            freq[i]-=1
    arr.sort()
    t=int(len(arr)/2)
    if len(arr)%2==0:
         L=arr[:t]
         U=arr[t:]
    else:
         L=arr[:t]
         U=arr[t+1:]   
    print(round(float(median(U)-median(L)),1))     

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
