#!/bin/python3
from statistics import mean
import math as m
import os
import random
import re
import sys

    

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
am=mean(arr)
oarr=[]
for i in range(len(arr)):
        v=(arr[i]-am)**2
        oarr.append(v)
soarr=sum(oarr)
print(round(m.sqrt(float(soarr/len(arr))),1))
