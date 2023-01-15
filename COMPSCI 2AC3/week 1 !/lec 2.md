# Lecture 2 Notes

## Goal: Studying various models of computation

Say we have a function:  
$ f: A \rightarrow B $  
$ x \in A \rightarrow [ f ] \rightarrow y \in B $  

We want to "compute" $f$  

The computation involves a "finite" set of operations (chosen from a finite and predefined set of operations) that are applied to $x$, generating output $f(x)$  

The set of predefined operations and the way we give the input and take the output define our computational model

We say $f$ is computable in our model if we can find a finite set of operations (a program) that gives the right output all the time for every $ x \in A $

### The Scramble Machine

- the machine has an infinite number of rows
- some of the rows may contain a finite number of balls.
- there is a lever that points to a row
- we have operations to manipulate the balls or the lever
- the machine has a single bit of memory, which we denote `MEM` (`MEM = false` or `true`)

> [o o o o o o o] $\leftarrow$  
> [&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;]  
> [&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;]  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ...  
> [&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;]  

#### Operations:

`LOWER_LEVER`:
- the lever goes to one row below it

`RAISE_LEVER`:
- the lever goes to one row above it

`CHECK_EMPTY`: 
- checks whether the row that the lever points to is empty
- if it is empty, `MEM = true`, otherwise `MEM = false`

`RESET_BALLS`:
- puts all the balls in the first row

`SCRAMBLE_DOWN`:  
> Example:  
> [o o o o]  
> [&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;] $\leftarrow$  
> &nbsp; &nbsp; &nbsp; $\Downarrow$ after scrambling  
> [&nbsp; &nbsp;o o &nbsp; ]  
> [&nbsp; &nbsp;o o &nbsp; ] $\leftarrow$  

- the balls in rows above the lever will start to fall down until the number of balls in each row above the lever is $\leq$ to its bottom row
- at the end, if any ball moved, `MEM = true`, otherwise `MEM = false`

> Another example:  
> [o o o &nbsp; &nbsp; &nbsp;]  
> [o o o o o]  
> [o o &nbsp; &nbsp; &nbsp; &nbsp; ] $\leftarrow$  
> [o &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;]  
> &nbsp; &nbsp; &nbsp; &nbsp;$\Downarrow$ after scrambling  
> [o o o &nbsp; &nbsp; &nbsp;]  
> [o o o &nbsp; &nbsp; &nbsp;]  
> [o o o o &nbsp; ] $\leftarrow$  
> [o &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;]

`SCRAMBLE_UP`:
- the balls in rows on or above the lever will start to rise until the number of balls in each row on or above the lever is smaller or equal to it's above row
- at the end. if any ball moved, `MEM = true`, otherwise `MEM = false`

> Example:  
> [o o &nbsp; ]  
> [o o o]  
> [o o &nbsp; ] $\leftarrow$  
> [o o &nbsp; ]  
> &nbsp; &nbsp;$\Downarrow$ after scrambling  
> [o o o]  
> [o o &nbsp; ]  
> [o o &nbsp; ] $\leftarrow$  
> [o o &nbsp; ]  

---
These terminate the program only if the condition holds:
```
Conditions:

RETURN_FALSE_IF_MEM_IS_FALSE
RETURN_FALSE_IF_MEM_IS_TRUE
RETURN_TRUE_IF_MEM_IS_FALSE
RETURN_FALSE_IF_MEM_IS_FALSE
```

Loop:
- loops over operations forever

```
operations: 

condition 1
condition 2
condition 3
```

### Example using Scramble Machine

Assume $ x \in \N $ and we want to compute whether $x$ is even or not

$f(x) \left\{ \begin{array}{ll} \text{true, x is even} \\ \text{false, x is odd} \end{array} \right. $

Assume we put the same number of balls as x on the first row and the lever points to the first row.

Write a program that computes $f$?

```
LOWER_LEVER
SCRAMBLE_DOWN
SCRAMBLE_UP
RETURN_TRUE_IF_MEM_IS_FALSE
RETURN_FALSE_IF_MEM_IS_TRUE
```

### Thoughts for next lecture:

(1) Write a program that determines if $x \in \N$ is a prime number

$f(x) \left\{ \begin{array}{ll} \text{true, x is prime} \\ \text{false, x is not prime} \end{array} \right. $

(2) Is there a simple $f$ that cannot be implemented with our scramble machine?