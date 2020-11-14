import time
import threading



i = 149
numbers = []



#slowsort von Angabe
def slowsort(A, i, j):
    if i >= j:
        return
    m = (i+j)//2
    slowsort(A, i, m)
    slowsort(A, m+1, j)
    if A[m] > A[j]:
        A[m],A[j] = A[j],A[m]
    slowsort(A, i, j-1)

#
def print_result():
    print(numbers)

while i >= 0:
    numbers += [i]
    i -= 1

start = int(round(time.time() * 1000))
slowsort(numbers, 0, len(numbers) - 1)
stop = int(round(time.time() * 1000))
difference = stop - start
print(str(difference / 1000), " s")