#!/usr/bin/python3
import math
import time
import threading

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


def startSlowsort(A, i, j):
    #print("A: ", A)
    numbersL = []
    numbersR = []

    index = 0
    while index <= j:
        if index <= int(j/2):
            numbersL.append(A[index])
        else:
            numbersR.append(A[index])
        index += 1

    #print("L: ", len(numbersL), numbersL)
    #print("R: ", len(numbersR) ,numbersR)

    t1 = threading.Thread(slowsort(numbers, 0, len(numbersL) - 1))
    t2 = threading.Thread(slowsort(numbers, 0, len(numbersR) - 1))
    t1.start()
    t2.start()




numbers = []
i = 149
while i >= 0:
    numbers += [i]
    i -= 1

print(numbers)
print("sorting...")
start = int(round(time.time() * 1000))

startSlowsort(numbers, 0, len(numbers) - 1)

stop = int(round(time.time() * 1000))
print(numbers)
difference = stop - start
print(str(difference / 1000), " s")
