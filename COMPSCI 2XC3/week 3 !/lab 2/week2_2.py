import timeit
import random
import matplotlib.pyplot as plot


def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L


def experiement1(n, m, step):
    times = []
    for i in range(0, n, step):
        L = create_random_list(i, i)
        time = 0
        for _ in range(m):
            start = timeit.default_timer()
            L2 = L.copy()
            end = timeit.default_timer()
            time += end - start
            times.append(time)
    return times


def experiement2(n, m):
    times = []
    L = create_random_list(n, n)
    for i in range(n):
        time = 0
        for _ in range(m):
            start = timeit.default_timer()
            x = L[i]
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
    return times


def experiement3(n):
    times = []
    L = []
    for i in range(n):
        time = 0
        start = timeit.default_timer()
        L.append(i)
        end = timeit.default_timer()
        times.append(end - start)
    return times

def experiement4(n):
    times = []
    for i in range(n):
        start = timeit.default_timer()
        fib(i)
        end = timeit.default_timer()
        times.append(end - start)
    return times

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

times = experiement3(10000000)
plot.plot(times)
plot.show()
