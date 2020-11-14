#!/usr/bin/python3
import math
import threading
import time
import numpy as np


def slowsort(A, i, j):
    if i >= j:
        return
    m = math.floor((i + j) / 2)
    slowsort(A, i, m)
    slowsort(A, m + 1, j)
    if A[j] < A[m]:
        tmp = A[m]
        A[m] = A[j]
        A[j] = tmp
    slowsort(A, i, j - 1)


numbers = []
i = 599
while i >= 0:
    numbers += [i]
    i -= 1

print("sorting...")
start = int(round(time.time() * 1000))

# 50 ~0.016
# 60 ~0.015-0.016
threadCount = 60
step = int(len(numbers) / threadCount)

numberArrays = []
numbers1 = [int(numbers[i]) for i in range(len(numbers)) if i < step * 1]
t1 = threading.Thread(slowsort(numbers1, 0, len(numbers1) - 1))
t1.start()
numberArrays.append(numbers1)

for multi in range(2, threadCount + 1):
    tmp = []
    tmp = [int(numbers[i]) for i in range(len(numbers)) if step * (multi - 1) <= i < step * multi]
    t = threading.Thread(slowsort(tmp, 0, len(tmp) - 1))
    t.start()
    numberArrays.append(tmp)

numbers = []
counter = threadCount - 1
while counter >= 0:
    for arrNumbers in numberArrays[counter]:
        numbers.append(arrNumbers)
    counter -= 1

stop = int(round(time.time() * 1000))

print(len(numbers))
print(numbers)
difference = stop - start
print(str(difference / 1000), " s")

# 0.019
