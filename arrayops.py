__author__ = 'BisharaKorkor'

import numpy as np
from math import sqrt, pow

def mean(array):
    """this function computes the mean of the values of a 1-D array"""
    totalsum = 0.

    for element in array:
        totalsum += element

    return (totalsum / len(array))


def stddev(array):
    """this function computes the standard deviation of a 1-D array"""
    mn = mean(array)
    td = 0. #sum of squared deviations

    print mn
    print np.average(array)

    for el in array:
        td += pow(mn - el, 2)

    print sqrt(td/(len(array)))
    print np.std(array)

    return sqrt(td / len(array))

def difference_of_averages(array1, array2):
    return mean(array2)-mean(array1)