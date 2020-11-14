import time
import threading

start_time = time.time()

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

t1 = threading.Thread(target=slowsort, args=(numbers, 0, len(numbers)-1,))

t1.start()
t1_start_time = time.time()

while_time = time.time()
t1.join()
t1_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t1.name, t1_end_time - t1_start_time))
while_end_time = time.time();

print(numbers)

print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (while_end_time - while_time))