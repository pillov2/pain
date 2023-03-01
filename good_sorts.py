
import random
import timeit
import math
import matplotlib.pyplot as plot



"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""
# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************
# ************ Dual Quick Sort ************

def dual_quicksort(l):
    random.shuffle(l)
    sort(l,  0, len(l)-1)


def sort(l, low, high):
    if(high <= low): return

    if(l[high] < l[low]): swap(l, low, high)

    lt, gt = low + 1, high - 1

    i = low + 1

    while (i<=gt):
        if(l[i] < l[low]): 
            swap(l, lt, i)
            i+=1
            lt+=1
        elif(l[high] < l[i]):
            swap(l, i, gt)
            gt-=1
        else:
            i+=1
    swap(l,low,lt-1)
    if(l[lt] < l[gt]): sort(l, lt+1, gt-1)
    sort(l,gt+1,high)

# *****************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************
def bottom_up_mergesort(l: list):
    length = len(l)
    end = length-1
    temp = l.copy()
    i=1
    while i<= end:
        for bot in range(0,end,i+i):
            mid = bot+i-1
            top = min(bot+i+i-1, end)
            merge1(l, temp, bot, mid, top)
        i = i * 2


# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.map = {}
        for i in range(len(self.data)):
            self.map[self.data[i]] = i
        self.build_heap()


    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.map[self.data[i]], self.map[self.data[largest_known]] = i, largest_known
            self.heapify(largest_known) 

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def contains(self, value):
        return value in self.data
    
    def increase_key(self, value, shift):        
        self.data[self.map[value]] += shift 
        self.bubble_up(self.map[value])
        
        

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            self.map[self.data[i]], self.map[self.data[self.parent(i)]] = i, self.parent(i)
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.map[self.data[0]], self.map[self.data[self.length - 1]] = 0, self.length - 1
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************
# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value





def normalTest(L, sort):
    start = timeit.default_timer()
    sort(L)
    end = timeit.default_timer()
    return (end - start)


total1 = 0
total2 = 0
total3 = 0
times1 = []
times2 = []
times3 = []
n = 1000
k = 1000
runs = 50

for i in range(n):
    print(i, "out of", n)
    for j in range(runs):
        og = create_random_list(i,k)
        L = og.copy()
        L2 = og.copy()
        L3 = og.copy()
        total1 += normalTest(L,quicksort)
        total2 += normalTest(L2,heapsort)
        total3 += normalTest(L3,mergesort)

    times1.append(total1/runs)
    times2.append(total2/runs)
    times3.append(total3/runs)
    total1,total2,total3 = 0, 0, 0

plot.plot(times1, label='Quick Sort')
plot.plot(times2, label= 'Heap Sort')
plot.plot(times3, label= 'Merge Sort')
plot.xlabel("List Length")
plot.ylabel("Time")
plot.legend()
plot.show()

#exp 6

n = 250

for i in range(n):
    temptime = []
    dualtemptime = []
    print(i)
    for j in range(50):
        l = create_near_sorted_list(2500,2500,n)
        l2 = l.copy()

        start = timeit.default_timer()
        quicksort(l)
        end = timeit.default_timer()

        temptime.append(end - start)

        start = timeit.default_timer()
        dual_quicksort(l2)
        end = timeit.default_timer()

        dualtemptime.append(end - start)

    times.append(sum(temptime)/20)
    dualtimes.append(sum(dualtemptime)/20)
    
print(sum(times) / sum(dualtimes))

plot.plot(times, label='QuickSort')
plot.plot(dualtimes, label='DualQuickSort')
plot.title("Swaps v.s. Time")
plot.xlabel("Swaps")
plot.ylabel("Time")
plot.legend()
plot.show()

#Exp 7
n = 2500

for i in range(n):
    temptime = []
    dualtemptime = []
    print(i)
    for j in range(25):
        l = create_random_list(i,i)
        l2 = l.copy()

        start = timeit.default_timer()
        mergesort(l)
        end = timeit.default_timer()

        temptime.append(end - start)

        start = timeit.default_timer()
        bottom_up_mergesort(l2)
        end = timeit.default_timer()

        dualtemptime.append(end - start)

    times.append(sum(temptime)/20)
    iterativetimes.append(sum(dualtemptime)/20)

plot.plot(times, label='MergeSort')
plot.plot(iterativetimes, label='BottomUpMergeSort')
plot.title("List Length v.s. Time")
plot.xlabel("List Length")
plot.ylabel("Time")
plot.legend()
plot.show()