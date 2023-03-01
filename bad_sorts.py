"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plot


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


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


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

# Optimized Bubble Sort
def bubble_sort2(L):
    for i in range(len(L)):
        flag = False
        max = L[i]
        for j in range(len(L) - i - 1):
            if flag == True:
                if L[j+1] > max:
                    L[j] = max
                    max = L[j+1]
                else:
                    L[j] = L[j + 1]
            else:
                if L[j+1] < L[j]:
                    max = L[j]
                    flag = True
                    L[j] = L[j+1]
        if flag == True:
            L[len(L)-i-1] = max
        




# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

# Optimized Selection sort

def selection_sort2(L):
    j = len(L) - 1
    for i in range(len(L)//2):
        min = L[i]
        max = L[i]
        min_i = i
        max_i = i
        for k in range(i, j + 1, 1):
            if (L[k] > max):
                max = L[k]
                max_i = k
            elif (L[k] < min):
                min = L[k]
                min_i = k

        swap(L,i,min_i)
 
        if (L[min_i] != max):
            swap(L,j,max_i)
        else:
            swap(L,j,min_i)

        j -= 1


def normalTest(L, sort):
    start = timeit.default_timer()
    sort(L)
    end = timeit.default_timer()
    return (end - start)

def sortTest(L, sort1, sort2):
    L2 = L.copy()
    sort1(L)
    sort2(L2)
    if(L == L2):
        print("passed")
    else:
        print("FAILED")


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
        og = create_random_list(i, k)
        L = og.copy()
        L2 = og.copy()
        L3 = og.copy()
        total1 += normalTest(L,selection_sort)
        total2 += normalTest(L2,selection_sort2)
        total3 += normalTest(L3,insertion_sort2)

    times1.append(total1/runs)
    times2.append(total2/runs)
    times3.append(total3/runs)
    total1,total2,total3 = 0, 0, 0

plot.plot(times1, label='Selection Sort')
plot.plot(times2, label= 'Selection Sort2')
plot.plot(times3, label= 'Insertion Sort')
plot.xlabel("List length")
plot.ylabel("Times")
plot.legend()
plot.show()
