# Lecture 1 Notes

### Course Outline Notes

- *R in Action* by Robert Kabacoff [Textbook]

### Lecture Notes  

Data Analysis involves:
- transforming the data
- imputation of missing values
    - ex: filling in missing data based on average information
- variable selection
    - may not need all available variables to form conclusions/predictions
- statistical modelling

Modern Data Analytics also includes:
- pulling data from a variety of sources, such as database management systems, text files, spreadsheets, a variety of different statistical packages, and web pages
- merging of obtained from different sources
- data cleaning
    - how are you going to deal with incomplete information
        - easiest way would be to delete the observation but may cause biases and is not preferred
- analysis with modern techniques such as *Machine Learning* techniques
- creating graphical displays of results
    - models (?)

About R
- an environment and a programming language used for statistical computing
    - mainly used by statisticians
- open sourced (ie. free)
- many powerful graphic packages, ex: ggplot2
- results from any step in an analysis can be saved, manipulated, and used as a new input
- R functionality can be integrated into other languages eg. C++, Python, SAS
- R can run on basically any platform, eg. MacOS, Windows

- Download from CRAM
http://cran.rproject.org


R Basics:
- case sensitive
- an interpreted language
- can enter commands in the prompt line, recommend runnings commands from a source file
- objects can be created and manipulated
    - object is anything that can be assigned a value, eg. data, results
    - objects must have a class attribute, which tells R how to handle is correctly
- <- is used for assignments !!not =
    - -> can also be used but is not standard convention
- use # to comment code

Language Type:
- any program is a set of instructions
- both compiled and interpreted languages take human-readable code and converts it into machine code, which can be read by a computer
- with compiled languages, the target machine translates the program
- compiled languages
    - directly converted into machine code, which the target machine executes   
    - fast
    - allows control of aspects such as memory and CPU use
    - must be mentually compiled before execution
- interpreted languages
    - use an interpreter, which executes the program line by line
    - usually slower to execute, relative to compiled languages
    - main advantage: because an interpreter is used, it is platform independent

- R interface is very simple
- most people use R studio
- RStudio Desktop
    - https:www.rstudio.com/products/rstudio/#rstudio-desktop
- RStudio uses multiple windows, has toold for importing data, visualizing input

The Workspace
- includes all user defined objects, such as vectors, matrices, functions, data frames and lists
- working directory is where R reads files from, and will save files to by default unless told otherwise

Packages
- packages are collections of R functions, data, and code,
- R comes with built in packages, you can download and install other packages that are of use to you
- must load a package into your coding session to be able to access it
- packags are stored in the library directory
- .libPaths() tells you where library is located
- library() shows you what packages are in your library

Notes
- c() is a combine functions that combines its arguments into a vector or list
- cor() is the measure of linear relationship between two variables
- plot(x,y) creates a basic scatter plot graph with the two variables inputted, where x and y are the axis'
    - can use external packages to fancier packages
- help.start() to access help page with tutorials about R and data imports in R
- to install a package vcd (for visualizing categorical data):
    - install.packages("vcd")
        - click on ontario mirror, or canadian, or close by??
- !! must remember to call packages every time you open R
    - updating R will remove all installed packages
- help(package="vcd")
- library(vcd) to load the library
- help(Arthritis) to get documentation on library?
- ordered factors have some form of order, regular factors can have any number to represent it
    - use stratify to check if R is reading the values correctly, to see if it is treating the factor as a factor or as an ordered factor
- head(Arthritis) to get the first six lines of code that is being pulled from your dataset
- str(Arthritis) to get type of variables, ex: factors with 2 levels, ordered factors with 3 levels, int
- xtabs to create a contingency table
    - cross-classifying variables are separated by +
    - only looking at female patients
    - art <- xtabs(~ Treatment + Improved, data = Arthritis, subset = Sex == "Female")
        - put into variable so you can call table after compiling
- ?xtabs can also be used to access function documentation


