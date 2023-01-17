# Lecture 3 Notes

## Data Input

### Introduction

- *R* can import data from flat files, statistical packages, spreadsheets, web files and databases
- *R* base functions include:
    - `read.csv()`
    - `read.delim()`
        - they are both wrapper functions that implement `read.table()` with specific defaults

### Text Files

- import data from delimited text files using `read.table()`
    - reads a file in table format and saves it as a data frame
    - by default, it converts character variables to factors
        - `stringsAsFactors = FALSE` suppresses this behaviour
            - can also use `colClasses` to specify the class of each column individually

### Importing via Connections

- *R* also allows you to import data via connections
- `file()` to access files, clipboard, and C-level standard input
- `url()` to access internet files through a URL that includes *http://, ftp://, or file://* 
    - for *http://* and *ftp://* URL's, proxies can be specified
    - complete URLs surrounded by double quotation marks can often be used directly in place of filenames