'''
Created on Dec 26, 2017

@author: jghuf
'''
import numpy as np
import time

def greatestNumber(matrix):
    greatestNumber = 0
    # Find the greatest number Up/Down
    for i in range(0,17):
        for j in range(0,20):
            res = matrix[i][j]* matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j] 
            if res > greatestNumber:
                greatestNumber = res
    
    # Find the greatest number Left/Right               
    for i in range(0,20):
        for j in range(0,17):
            res = matrix[i][j]* matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3] 
            if res > greatestNumber:
                greatestNumber = res
    
    #Find the greatest number diagonally from Left Up to Right Down
    for i in range(0,16):
        for j in range(0,16):
            res = matrix[i][j]* matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3] 
            if res > greatestNumber:
                greatestNumber = res
    
    #Find the greatest number diagonally from Right Up to Left Down
    for i in range(3,20):
        for j in range(0,16):
            res = matrix[i][j]* matrix[i-1][j+1] * matrix[i-2][j+2] * matrix[i-3][j+3] 
            if res > greatestNumber:
                greatestNumber = res
    
    return greatestNumber



if __name__ == '__main__':
    start = time.time()
    
    file = 'grid.txt'
    m = np.zeros((20,20))
    with open(file) as f:
        for i,line in enumerate(f):
            splittedLine = line.split()
            for j,sL in enumerate(splittedLine):
                m[i][j] = sL
            
    greatestNumber = greatestNumber(m)
    
    elapsed = (time.time() - start)
 
    print("Greatest number %s found in %s seconds" % (greatestNumber,elapsed))

    