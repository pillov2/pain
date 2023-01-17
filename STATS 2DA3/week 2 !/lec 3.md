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

### Importing Web Data

- extract data from the web by using webscraping or an API (application programming interface)
    - webscraping involves extracting information from a webpage(s) and storing it in a format suitable for *R* for further analysis
- `revest` package has functions for simplifying the extraction of data from web pages
- API's allow access to online data stores and web services
    - act as a go-between for your programming package and the data source that you are accessing, allowing different software components to interact with each other correctly
- can access Twitter data through `twitteR`, Facebook data via `Rfacebook` and Flickr via `Rflickr`

### Simsom's Paradox

> TODO ADD IMAGE EXAMPLE FROM CLASS