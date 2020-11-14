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


numbers = []
i = 149
while i >= 0:
    numbers += [i]
    i -= 1

print(numbers)
print("sorting...")
start = int(round(time.time() * 1000))

anzahlThreads = 8
step = len(numbers) / anzahlThreads

numbers1 = [int(numbers[i]) for i in range(len(numbers)) if i < step * 1]
numbers2 = [int(numbers[i]) for i in range(len(numbers)) if step <= i < step * 2]
numbers3 = [int(numbers[i]) for i in range(len(numbers)) if step * 2 <= i < step * 3]
numbers4 = [int(numbers[i]) for i in range(len(numbers)) if step * 3 <= i < step * 4]
numbers5 = [int(numbers[i]) for i in range(len(numbers)) if step * 4 <= i < step * 5]
numbers6 = [int(numbers[i]) for i in range(len(numbers)) if step * 6 <= i < step * 7]
numbers7 = [int(numbers[i]) for i in range(len(numbers)) if step * 7 <= i < step * 8]
numbers8 = [int(numbers[i]) for i in range(len(numbers)) if i >= step * 8]


t1 = threading.Thread(slowsort(numbers1, 0, len(numbers1) - 1))
t2 = threading.Thread(slowsort(numbers2, 0, len(numbers2) - 1))
t3 = threading.Thread(slowsort(numbers3, 0, len(numbers3) - 1))
t4 = threading.Thread(slowsort(numbers4, 0, len(numbers4) - 1))
t5 = threading.Thread(slowsort(numbers5, 0, len(numbers5) - 1))
t6 = threading.Thread(slowsort(numbers6, 0, len(numbers6) - 1))
t7 = threading.Thread(slowsort(numbers7, 0, len(numbers7) - 1))
t8 = threading.Thread(slowsort(numbers8, 0, len(numbers8) - 1))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

numbers = []
for i in numbers8:
    numbers.append(i)
for i in numbers7:
    numbers.append(i)
for i in numbers6:
    numbers.append(i)
for i in numbers5:
    numbers.append(i)
for i in numbers4:
    numbers.append(i)
for i in numbers3:
    numbers.append(i)
for i in numbers2:
    numbers.append(i)
for i in numbers1:
    numbers.append(i)

stop = int(round(time.time() * 1000))
print(numbers)
difference = stop - start
print(str(difference / 1000), " s")
