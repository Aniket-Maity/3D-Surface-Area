#!/bin/python3

import math
import os
import random
import re
import sys
def contribution_height(current, previous): 
    return abs(current - previous); 
# Complete the surfaceArea function below.
def surfaceArea(A):
    
    ans = 0; 
  
    for i in range(H):  
        for j in range(W):  
            up = 0;  
            left = 0; 
            if (i > 0): 
                up = A[i - 1][j]; 
            if (j > 0): 
                left = A[i][j - 1]; 
            ans += contribution_height(A[i][j], up)+contribution_height(A[i][j], left); 
            if (i == H - 1): 
                ans += A[i][j]; 
            if (j == W - 1): 
                ans += A[i][j]; 
    ans += H * W * 2
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
