#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s1):
    """for i  in range(len(s1)):
         if s1[i]==' ':
              j=i
              s2=s1[i+1].upper()
    return(s1[0].upper()+ s1[1:j]+ ' ' +s2+s1[j+2:])"""
    s2=''
    """for i in s1.split(' '):
        #i=i.capitalize()
        s2=s2+i.capitalize()
    return(' '.join(s2))"""
    return(' '.join(i.capitalize() for i in s1.split(' ')))#main line of code
if __name__ == '__main__':
