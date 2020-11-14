import time
import threading

start_time = time.time()

n = 149



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

threads = []
list = []

list1 = numList[0:50]
list2 = numList[50:100]
list3 = numList[100:150]

list.append(list1)
list.append(list2)
list.append(list3)
print("L: ", len(list1), list1)
print("R: ", len(list2), list2)
print("M: ", len(list3), list3)

for i in range(0, 2):
    t = threading.Thread(target=slowsort, args=(list[i], 0, len(list[i])-1,))
    threads.append(t)

for t in threads:
    t.start()

print(list1)
list1.reverse()
print(list1)

list2.extend(list1)
list3.extend(list2)
print(list3)

print("--- %s seconds ---" % (time.time() - start_time))

