# from R in Action by Kabacoff

#note:  rm(list=ls()) clears the memory

#############VECTORS

#There are 3 types of vector 

#a = Numeric
a <- c(1, 2, 5, 3, 6, -2, 4)

#b= Characterb <- c("one", "two", "three")

#c= Logicalc <- c(TRUE, TRUE, TRUE, FALSE, TRUE, FALSE)

#refer to the second and fourth elements of vector a
d<-a[c(2, 4)]
d

#generate a sequence of numbers
e<- c(2:6)
e

# one more bracket and ":" example, compare

f<- c("k", "j", "h", "a", "c", "m")
g<- f[c(1, 3, 5)]
g

h<-f[2:6]
h

#############MATRICES

#format
newmatrix <- matrix(vector, nrow=number_of_rows, ncol=number_of_columns,byrow=logical_value, dimnames=list(char_vector_rownames, char_vector_colnames))

#vector contains the elements for the matrix,
#nrow and ncol specify the row and column dimensions
#byrow indicates whether the matrix should be filled in by row (byrow=TRUE) or by column (byrow=FALSE). The default is by column.
#dimnames contains optional row and column labels stored in character vectors

y <- matrix(1:20, nrow=5, ncol=4)
y

#X[i,] refers to the ith row of matrix X
#X[,j] refers to the jth column  
#X[i, j] refers to the ijth element

x <- matrix(1:10, nrow=2)
x

ab<-x[2,]
ab

bc<-x[,2]
bc

#first row, 4th and 5th elements (columns)
cd<-x[1, c(4,5)]
cd

#############Arrays
# a 3D, (2 × 3 × 4) array of numbers

dim1 <- c("A1", "A2")dim2 <- c("B1", "B2", "B3")dim3 <- c("C1", "C2", "C3", "C4")z <- array(1:24, c(2, 3, 4), dimnames=list(dim1, dim2, dim3))z

#compare without dimnames
dim1 <- c("A1", "A2")
dim2 <- c("B1", "B2", "B3")
dim3 <- c("C1", "C2", "C3", "C4")
z <- array(1:24, c(2, 3, 4))
z

#############DATA FRAMES
#create a data frame
patientID <- c(1, 2, 3, 4)age <- c(25, 34, 28, 52)diabetes <- c("Type1", "Type2", "Type1", "Type1")status <- c("Poor", "Improved", "Excellent", "Poor")patientdata <- data.frame(patientID, age, diabetes, status)patientdata

#To select a column in R you can use brackets,e.g. DataFrameName[ ] 
#specify elements by column number 
ef<-patientdata[1:2]
ef

#specify elements by column name
gh<-patientdata[c("diabetes", "status")]
gh

#lets look at the age variable
ij<-patientdata$age
ij

#produce a table of diabetes "type" against "age"
table <-table(patientdata$diabetes, patientdata$status)
table

#############FACTORS

#enter the data as vectors
patientID <- c(1, 2, 3, 4)age <- c(25, 34, 28, 52)diabetes <- c("Type1", "Type2", "Type1", "Type1")status <- c("Poor", "Improved", "Excellent", "Poor")

#define "diabetes" and "status" as factorsdiabetes <- factor(diabetes)status <- factor(status, order=TRUE)

#combine the data into a dataframe
patientdata <- data.frame(patientID, age, diabetes, status) 

#I always use the str()command to get an overview of the dataset 
#I'm using, and in a cse like this, to make sure that my variables 
#are being read by R in the correct format.str(patientdata)

#note: we happened to get the correct order for our levels for "status" using the defaut setting, as alphabetically it works here. 

#we can over-ride the alphabetical ordering of levels
status <- factor(status, order=TRUE,levels=c("Poor", "Improved", "Excellent"))

#############LISTS

#string
g <- "My List" 

#numeric vectorh <- c(25, 26, 18, 39)

#matrixj <- matrix(1:10, nrow=5)

#character vectork <- c("one", "two", "three")

#create a listmylist <- list(title=g, ages=h, j, k) mylist

#print the second component, call by number
mylist[[2]]

#print the second component, call by variable namemylist[["ages"]]
