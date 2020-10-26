"""
Python With Numpy
Jeffrey Lansford
Program 4
9/28/2020
Python Implmentation of Gauss Elimination with back substition using Numpy
"""
import json
import random
import sys
import time

import numpy as np


def createArray(size):
    """
    to create an matrix of random numbers between 1 and 20 with a given size

    size    --size of matrix, N x N+1
    """
    n = np.zeros((size, size + 1))
    for x in range(size):
        for y in range(size + 1):
            n[x, y] = random.randint(1, 20)
    return n


def createArray_2(size):
    """
    to create an matrix of random numbers between 1 and 20 with a given size

    size    --size of matrix, N x N+1
    """
    a = np.zeros((size, size))
    b = np.zeros((size, 1))
    for x in range(size):
        for y in range(size):
            a[x, y] = random.randint(1, 20)
    for y in range(size):
        b[y, 0] = random.randint(1, 20)
    return (a, b)


def Gauss(n):
    """
    does Gauss Elimination with back substitution on a given matrix
    based on https://www.codesansar.com/numerical-methods/gauss-elimination-method-python-program.htm

    n   --matrix to do Gauss Elimination
    """
    size = len(n)

    # creates lower triangular matrix
    for i in range(size):
        for j in range(i + 1, size):
            ratio = n[j, i] / n[i, i]
            n[j] = n[j] - ratio * n[i]

    # Back substitution
    for i in range(size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            ratio = n[j, i] / n[i, i]
            n[j] = n[j] - ratio * n[i]
        n[i] = n[i] / n[i, i]


def Gauss_2(a, b):
    """
    does Gauss Elimination with back substion on a given matrix using the numpy solve linear equations function

    a   -- Coefficient Matrix
    b   -- Ordinate Matrix    
    """
    np.linalg.solve(a, b)


def test_case(size):
    """
    runs test cases on a given size of the matrix. records length of runtime Gauss Elimination and returns in milliseconds

    size    --size of matrix
    """
    n = createArray(size)
    start = time.perf_counter()
    Gauss(n)
    end = time.perf_counter()
    return (end - start) * 1000


def test_case_2(size):
    """
    runs test cases on a given size of the matrix. records length of runtime Gauss Elimination and returns in milliseconds

    uses Version 2 of Gauss Elimination

    size    --size of matrix
    """
    a, b = createArray_2(size)
    start = time.perf_counter()
    Gauss_2(a, b)
    end = time.perf_counter()
    return (end - start) * 1000


# Sample sizes
sizes = [250, 500, 1000, 1500, 2000]

# Store results into json file for eazy copying of data into excel
results = {"Version 1": {}, "Version 2": {}}

# Test Verison 1
# Run 5 test runs on the different sizes
print("Python with Numpy Version 1")
for i in range(5):
    print(f"test run {i+1}")
    results["Version 1"].update({f"Test Run {i+1}": {}})
    for size in sizes:
        a = test_case(size)
        results["Version 1"][f"Test Run {i+1}"].update({size: a})
        print("\t{:4}: {:} milliseconds".format(size, a))

# Test Version 2
print("Python with Numpy Version 2")
for i in range(5):
    print(f"test run {i+1}")
    results["Version 2"].update({f"Test Run {i+1}": {}})
    for size in sizes:
        a = test_case_2(size)
        results["Version 2"][f"Test Run {i+1}"].update({size: a})
        print("\t{:4}: {:} milliseconds".format(size, a))
y = json.dumps(results, indent=4)
f = open("resultsNumpy.json", "w")
f.write(y)
f.close()
