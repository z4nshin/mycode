import math

def prime(num):
    max = num/2

    for i in range(2, max):

        while( num%i==0 ):
            print i,
            num = num/i
    if num != 1:
        print num


prime(127146173)

