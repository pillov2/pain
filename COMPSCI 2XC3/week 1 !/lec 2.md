# Lecture 2 Notes

```python
import random
import timeit

# used to time the runtime
start = timeit.defualt_timer()

n = 0

for i in range(10):
    n += i;

end = timeit.default_timer()

print(end - start)

Output:
# first run
1.7699999999998162e-05

#second run
2.1999999999994246e-05

------------------------------------------------------------

runs = 10000
total_time = 0

for _ in range(runs):
    start = timeit.defualt_timer()
    n = 0

    for i in range(10):
        n += i;

    end = timeit.default_timer()
    total_time += end - start

print(total_time/runs)

OUTPUT:
# invariance between each run's runtime
5.1067e-06
```
> Note: runtimes are machine dependent, if you have a super computer, of course it'll have a faster runtime than a potato

BinarySearch = O( $logn$ ) [divide and conquer]  
InsertionSort = O( $n^2$ ) [typical rudimentary sorting algorithm]  

Why you might run empirical test cases:
- What if n is small? Big O is the time complexity as n $\rightarrow \infin$
- best/average/worst case
- may be variations/optimizations in implementation that affect the speed of the algorithm
    - it still grows with the same complexity, therefore it would still have the same complexity, but potentially different run times
- the constant factor c is hidden in big O notation, but c can be very very large
    - g(n) may look better than f(n) as n $\rightarrow \infin$, but in practice, we would never use g(n) because c is so large
- verification of algorithms, to see if it functions as intended

```Python
def binsearch1(value, values):
    left, right = 0, len(values) - 1

    while left < right:
        mid = (left + right) // 2

        if values[mid] == value:
            return True
        
        if values[mid] < value:
            # add one because python always rounds down when doing integer division, need to add one for base cases
            left = mid + 1

        else:
            right = mid
    
    # TODO
    return values

print(binsearch(3, [1, 2, 3, 4]))
print(binsearch(3, [1, 2, 4, 5]))
print(binsearch(3, [3]))
print(binsearch(3, [1]))

OUTPUT:
True
False
True
False
```

- when testing empirically, if we continously use the same sorted list, if the list does not have 500, the algorithm will ALWAYS run at its worst case scenario
    - we might see random large spikes in runtime due to this
- when we test with a new sorted list everytime, we are testing best, average, and worst case scenarios all together, so while it may have a larger runtime, it will have smaller invariants
- when looking at the ordering of `if statements`, if the statements at the beginning have low probability, putting them at the top would be like running an if statement that is not likely to be true

> [A has a low probability of occurring]  
> [B has a high probability of occurring]  
> 
> if A  
> if B  
> else (c)  
>
> if B has a higher probability, it is more likely to be true, therefore, we avoid checking statements that have a low probability of being true