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

numbersL = []
numbersR = []


numbersL = [int(numList[i]) for i in range(len(numList)) if i<75]
numbersR = [int(numList[i]) for i in range(len(numList)) if i >= 75]

print("L: ", len(numbersL), numbersL)
print("R: ", len(numbersR), numbersR)

#list1 = numList[0:n//2]
#list2 = numList[n//2:n+1]


t1 = threading.Thread(target=slowsort, args=(numbersL, 0, len(numbersL)-1,))
t2 = threading.Thread(target=slowsort, args=(numbersR, 0, len(numbersR)-1,))



t1.start()
t1_start_time = time.time()

t2.start()
t2_start_time = time.time()


t1.join()
t1_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t1.name, t1_end_time - t1_start_time))

t2.join()
t2_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t2.name, t2_end_time - t2_start_time))

#list2.extend(list1)
#print(list2)
arr = []
#arr = [int(numbersL[i]) for i in range(len(numbersL))]
#arr = [int(numbersR[i+75]) for i  in range(len(numbersR))]

for i in numbersR:
    arr.append(i)
for i in numbersL:
    arr.append(i)

print(arr)

print("--- %s seconds ---" % (time.time() - start_time))