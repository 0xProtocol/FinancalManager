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


threads = []
list = []

numbers1 = [int(numList[i]) for i in range(len(numList)) if i<50]
numbers2 = [int(numList[i]) for i in range(len(numList)) if ((i >= 50) & (i < 100))]
numbers3 = [int(numList[i]) for i in range(len(numList)) if ((i >= 100) & (i < 150))]
list.append(numbers1)
list.append(numbers2)
list.append(numbers3)

print("L: ", len(numbers1), numbers1)
print("R: ", len(numbers2), numbers2)
print("M: ", len(numbers3), numbers3)


for i in range(0, 2):
    t = threading.Thread(target=slowsort, args=(list[i], 0, len(list[i])-1,))
    threads.append(t)

for t in threads:
    t.start()


for i in numbers3[::-1]:
   arr.append(i)
for i in numbers2[::-1]:
    arr.append(i)
for i in numbers1[::-1]:
    arr.append(i)


print(arr)

print("--- %s seconds ---" % (time.time() - start_time))

#Thread: Thread-1 -- 0.0608367919921875 seconds --
#Thread: Thread-2 -- 0.025918245315551758 seconds --
#Thread: Thread-3 -- 0.008976459503173828 seconds --
#--- 0.07579684257507324 seconds ---