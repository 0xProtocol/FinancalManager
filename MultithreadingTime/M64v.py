import time
import threading

start_time = time.time()

n = 149
arr = []


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
    print(numList)

numList = list(range(n, -1, -1))

print(numList)



numbers1 = [int(numList[i]) for i in range(len(numList)) if i<50]
numbers2 = [int(numList[i]) for i in range(len(numList)) if ((i >= 50) & (i < 100))]
numbers3 = [int(numList[i]) for i in range(len(numList)) if ((i >= 100) & (i < 150))]

print("L: ", len(numbers1), numbers1)
print("R: ", len(numbers2), numbers2)
print("M: ", len(numbers3), numbers3)



t1 = threading.Thread(target=slowsort, args=(numbers1, 0, len(numbers1)-1,))
t2 = threading.Thread(target=slowsort, args=(numbers2, 0, len(numbers2)-1,))
t3 = threading.Thread(target=slowsort, args=(numbers3, 0, len(numbers3)-1,))


t1.start()
t1_start_time = time.time()

t2.start()
t2_start_time = time.time()

t3.start()
t3_start_time = time.time()

t1.join()
t1_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t1.name, t1_end_time - t1_start_time))

t2.join()
t2_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t2.name, t2_end_time - t2_start_time))

t3.join()
t3_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t3.name, t3_end_time - t3_start_time))

for i in numbers3:
    arr.append(i)
for i in numbers2:
    arr.append(i)
for i in numbers1:
    arr.append(i)

print(arr)

print("--- %s seconds ---" % (time.time() - start_time))

