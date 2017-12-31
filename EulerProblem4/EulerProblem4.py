'''
Created on Dec 31, 2017

@author: jghuf
'''
import time


def largestPalindrom():
    largest = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            product = i*j
            if (product > largest) and (str(product) == str(product)[::-1]):
                largest = product

    return largest

if __name__ == '__main__':
    start = time.time()
    largestPali =  largestPalindrom()
    elapsed = (time.time() - start)
 
    print("Largest palindrom number is %s , found in %s seconds" % (largestPali,elapsed))
