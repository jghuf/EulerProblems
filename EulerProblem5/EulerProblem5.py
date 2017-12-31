'''
Created on Dec 31, 2017

@author: jghuf
'''
import time

# if number is divisible by 20 than it also is divisible by 2 etc,
divList = [11, 13, 14, 16, 17, 18, 19, 20]


def number(limit):
    for num in range(limit,999999999,limit):
        if all((num % i == 0) for i in divList):
            return num


if __name__ == '__main__':
    limit = 20
    start = time.time()
    smallestMultiple =  number(limit)
    elapsed = (time.time() - start)
 
    print("The smallest multiple is %s , found in %s seconds" % (smallestMultiple,elapsed))
