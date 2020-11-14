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

numList = list(range(n, 0-1, -1))

print(numList)

list1 = numList[0:n//2]
list2 = numList[n//2:n+1]

#t1 = threading.Thread(target=slowsort, args=(list1, 0, len(list1)-1,))
#t2 = threading.Thread(target=slowsort, args=(list2, 0, len(list2)-1,))
slowsort(list1,0,len(list1)-1,)
slowsort(list2,0,len(list2)-1,)


list2.extend(list1)
print(list2)

print("--- %s seconds ---" % (time.time() - start_time))

#Thread: Thread-1 -- 0.3640248775482178 seconds --
#Thread: Thread-2 -- 0.37100768089294434 seconds --
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]
#--- 0.42386627197265625 seconds ---

#Thread: Thread-1 -- 0.061834096908569336 seconds --
#Thread: Thread-2 -- 0.04188799858093262 seconds --
#Thread: Thread-3 -- 0.009973764419555664 seconds --
#--- 0.0857701301574707 seconds ---
