"""
Python Without Numpy
Jeffrey Lansford
Program 4
9/28/2020
Python Implmentation of Gauss Elimination with back substition using without Numpy
"""
import json
import random
import sys
import time


def createArray(size):
    """
    to create an matrix of random numbers between 1 and 20 with a given size

    size    --size of matrix, N x N+1
    """
    n = []
    for x in range(size):
        n.append([])
        for _ in range(size + 1):
            n[x].append(float(random.randint(1, 20)))
    return n


def Gauss(n):
    """
    does Gauss Elimination with back substion on a given matrix
    based on https://www.codesansar.com/numerical-methods/gauss-elimination-method-python-program.htm

    n   --matrix to do Gauss Elimination
    """
    size = len(n)

    # creates lower triangular matrix
    for i in range(size):
        for j in range(i + 1, size):
            ratio = n[j][i] / n[i][i]
            for k in range(size + 1):
                n[j][k] = n[j][k] - ratio * n[i][k]

    # Back substitution
    for i in range(size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            ratio = n[j][i] / n[i][i]
            for k in range(size + 1):
                n[j][k] = n[j][k] - ratio * n[i][k]
        temp = n[i][i]
        for k in range(size + 1):
            n[i][k] = n[i][k] * (1.0 / temp)


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


# Sample sizes
sizes = [250, 500, 1000, 1500, 2000]

# Store results into json file for eazy copying of data into excel
results = {}

# Run 5 test runs on the different sizes
for i in range(5):
    print(f"test run {i+1}")
    results.update({f"Test Run {i+1}": {}})
    for size in sizes:
        a = test_case(size)
        results[f"Test Run {i+1}"].update({size: a})
        print("\t{:4}: {:} milliseconds".format(size, a))
y = json.dumps(results, indent=4)
f = open("resultsNotNumpy.json", "w")
f.write(y)
f.close()
