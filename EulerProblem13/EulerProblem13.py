'''
Created on Jan 1, 2018

@author: jghuf
'''
import time


if __name__ == '__main__':
    start = time.time()
    
    file = 'EP13.txt'
    
    num = 0
    with open(file) as f:
        for line in f:
            num = num + int(line)
            
    
    elapsed = (time.time() - start)
 
    print("First 10 digits of large sum %s found in %s seconds" % (str(num)[:10],elapsed))  