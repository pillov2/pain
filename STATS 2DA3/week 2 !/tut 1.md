# Tutorial 1 Notes

```R
# by putting braces outside of the function, it serves as a print function
print("Hello World")
("Hello World")

# initialize the vector
vec <- c(1, 2, 3, 4)

print("Sum of the vector")
sum(vec)

print("Mean of the vector")
mean(vec)

print("Product of the vector")
prod(vec)

# initiliaze vec again
vec <- c(1.1, NA, 2, 3.0, NA)

print("Sum of the vector")
sum(vec)

print("Mean of the vector with NA values")
mean(vec, na.rm = TRUE)

print("Mean of the vector without NA values")
mean(vec, na.rm = FALSE)

print("Product of the vector with NA values")
prod(vec, na.rm = TRUE)

print("Product of the vector without NA values")
prod(vec, na.rm = FALSE)

# checks if there are NA values within the data set
# will return the values within the vectors and state if it is NA or not (true or false)
is.na(vec)

# initialize vector car
CAR <- c("red", "green", "yellow")
print(CAR)

# prints class of vector's elements
class(CAR)

# initialize vector colours_CAR
colours_CAR <- c("green", "green", "yellow", "red", "red", "red", "green")
print(colours_CAR)

# make colours_CAR into a factor object with levels
factor_CAR <- factor(colours_CAR)
print(factor_CAR)

# prints out how many levels there are in our factor
(nlevels(factor_CAR))

# gives more information about factored car
str(factor_CAR)

# manually specify the order of factors
factor_CAR <- factor(colours_CAR, levels = c("green", "yellow", "red"))
str(factor_CAR)

# create matrix, filled by rows
matrix1 = matrix(data = c("a", "a", "b", "c", "b", "a"), nrow = 2, ncol = 3, byrow = TRUE)
print(matrix1)

# create matrix, filled by columns
matrix1 = matrix(data = c("a", "c", "a", "b", "b", "a"), nrow = 2, ncol = 3, byrow = FALSE)
print(matrix1)
```

```R
OUTPUT:
> # by putting braces outside of the function, it serves as a print function
> print("Hello World")
[1] "Hello World"
> ("Hello World")
[1] "Hello World"
> # initialize the vector
> vec <- c(1, 2, 3, 4)
> print("Sum of the vector")
[1] "Sum of the vector"
> sum(vec)
[1] 10
> print("Mean of the vector")
[1] "Mean of the vector"
> mean(vec)
[1] 2.5
> print("Product of the vector")
[1] "Product of the vector"
> prod(vec)
[1] 24
> # initiliaze vec again
> vec <- c(1.1, NA, 2, 3.0, NA)
> print("Sum of the vector")
[1] "Sum of the vector"
> sum(vec)
[1] NA
> print("Mean of the vector with NA values")
[1] "Mean of the vector with NA values"
> mean(vec, na.rm = TRUE)
[1] 2.033333
> print("Mean of the vector without NA values")
[1] "Mean of the vector without NA values"
> mean(vec, na.rm = FALSE)
[1] NA
> print("Product of the vector with NA values")
[1] "Product of the vector with NA values"
> prod(vec, na.rm = TRUE)
[1] 6.6
> print("Product of the vector without NA values")
[1] "Product of the vector without NA values"
> prod(vec, na.rm = FALSE)
[1] NA
> # checks if there are NA values within the data set
> # will return the values within the vectors and state if it is NA or not (true or false)
> is.na(vec)
[1] FALSE  TRUE FALSE FALSE  TRUE
> # initialize vector car
> CAR <- c("red", "green", "yellow")
> print(CAR)
[1] "red"    "green"  "yellow"
> # prints class of vector's elements
> class(CAR)
[1] "character"
> # initialize vector colours_CAR
> colours_CAR <- c("green", "green", "yellow", "red", "red", "red", "green")
> print(colours_CAR)
[1] "green"  "green"  "yellow" "red"    "red"    "red"   
[7] "green" 
> # make colours_CAR into a factor object with levels
> factor_CAR <- factor(colours_CAR)
> print(factor_CAR)
[1] green  green  yellow red    red    red    green 
Levels: green red yellow
> # prints out how many levels there are in our factor
> (nlevels(factor_CAR))
[1] 3
> # gives more information about factored car
> str(factor_CAR)
 Factor w/ 3 levels "green","red",..: 1 1 3 2 2 2 1
> # manually specify the order of factors
> factor_CAR <- factor(colours_CAR, levels = c("green", "yellow", "red"))
> str(factor_CAR)
 Factor w/ 3 levels "green","yellow",..: 1 1 2 3 3 3 1
> # create matrix, filled by rows
> matrix1 = matrix(data = c("a", "a", "b", "c", "b", "a"), nrow = 2, ncol = 3, byrow = TRUE)
> print(matrix1)
     [,1] [,2] [,3]
[1,] "a"  "a"  "b" 
[2,] "c"  "b"  "a" 
> # create matrix, filled by columns
> matrix1 = matrix(data = c("a", "c", "a", "b", "b", "a"), nrow = 2, ncol = 3, byrow = FALSE)
> print(matrix1)
     [,1] [,2] [,3]
[1,] "a"  "a"  "b" 
[2,] "c"  "b"  "a" 
```