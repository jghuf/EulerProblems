'''
Created on Dec 31, 2017

@author: jan
'''
import time 

def sumOfEvenFibonacci(limit):
    fib0 = 1
    fib1 = 1
    fib2 = 0
    sum = 0
    while fib2 < limit:
        fib2 = fib0 + fib1
        if (fib2 % 2) == 0:
            sum = sum + fib2
        fib0 = fib1
        fib1 = fib2
    return sum


if __name__ == '__main__':
    limit = 4000000
    start = time.time()
    sumofEven =  sumOfEvenFibonacci(limit)
    elapsed = (time.time() - start)
 
    print("Sum of even Fibonacci numbers up to "+ str(limit)+" is %s , found in %s seconds" % (sumofEven,elapsed))
