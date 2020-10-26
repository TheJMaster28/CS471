"""
Jeffrey Lansford
Program 4
9/23/2020
Python Implmentation of Gauss Elimination with back substition using Numpy
"""
import json
import random
import sys
import time

import numpy as np

np.set_printoptions(suppress=True)


def createArray(size):
    """
    to create an matrix of random numbers between 1 and 20 with a given size

    size    --size of matrix, N x N+1
    """
    n = np.zeros((size, size + 1))
    for x in range(size):
        for y in range(size + 1):
            n[x][y] = random.randint(1, 20)
    return n


def Gauss(n):
    """
    does Gauss Elimination with back substion on a given matrix
    based on https://www.codesansar.com/numerical-methods/gauss-elimination-method-python-program.htm

    n   --matrix to do Gauss Elimination
    """
    size = len(n)
    for i in range(size):
        for j in range(i + 1, size):
            if n[i][i] == 0:
                raise SystemError()

            ratio = n[j][i] / n[i][i]
            n[j] = n[j] - ratio * n[i]

    for i in range(size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            ratio = n[j][i] / n[i][i]

            if n[i][i] == 0:
                raise SystemError()

            n[j] = n[j] - ratio * n[i]
        n[i] = n[i]  / n[i][i]


def test_case(size):
    """
    runs test cases on a given size of the matrix. Times Gauss Elimination and returns how long it took to run

    size    --size of matrix
    """
    n = createArray(size)
    start = time.perf_counter()
    Gauss(n)
    end = time.perf_counter()
    return (end - start)


if __name__ == "__main__":
    # n = createArray(5)
    # Gauss(n)
    sizes = [250, 500, 1000, 1500, 2000]
    # sizes = [250]
    results = {}
    for i in range(5):
        print(f"test run {i+1}")
        results.update({f"Test Run {i+1}": {}})
        for size in sizes:
            a = test_case(size)
            results[f"Test Run {i+1}"].update({size: a})
            print(f"\tfinshed with {size}")
    y = json.dumps(results, indent=4)
    f = open("resultsNumpy.json", "w")
    f.write(y)
    f.close()
    print(y)
