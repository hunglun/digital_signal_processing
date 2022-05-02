#!/bin/env python3
"""
Digital Noise Generation
"""
import matplotlib.pyplot as plt
import sys
from random import random


def get_sample(n):
    """
    n is the number of random numbers used to create a sample.
    sample x = = RAND_1 + RAND_2 + .. + RAND_n
    """
    assert(n>0)
    if n == 1:
        return random()
    else:
        return random() + get_sample(n-1)

    
def generate_histogram(sample_size, bin_size, n):
    """
    each sample x = RAND_1 + RAND_2 + .. + RAND_n
    bin_size = how many samples in a bin
    """
    assert(sample_size > bin_size)    
    data = []
    for i in range(sample_size):
        data.append(get_sample(n))
    assert(len(data) ==  sample_size)
    print("bins", int(sample_size/bin_size))
    plt.hist(data, int(sample_size/bin_size))
    plt.show()


# run :  pytest-3 <this_program>
# close the pop up histogram to see next histogram
def test_1():
    generate_histogram(100000, 100, 1)

def test_2():
    generate_histogram(100000, 100, 2)

def test_3():
    generate_histogram(100000, 100, 3)

def test_4():
    generate_histogram(100000, 100, 4)

def test_5():
    generate_histogram(100000, 100, 5)
    

def test_6():
    generate_histogram(100000, 100, 6)

def test_7():
    generate_histogram(100000, 100, 7)

def test_8():
    generate_histogram(100000, 100, 8)

def test_9():
    generate_histogram(100000, 100, 9)

def test_10():
    generate_histogram(100000, 100, 10)

def test_11():
    generate_histogram(100000, 100, 11)
    
def test_12():
    generate_histogram(100000, 100, 12)
    
if __name__ == "__main__":
    generate_histogram(int(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))

    
    
