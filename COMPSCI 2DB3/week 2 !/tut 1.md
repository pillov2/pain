# Tutorial 1 Notes

## General SSH Setup

To connect to the server using SSH:  

```
ssh linc94@cs2db3.cas.mcmaster.ca
```

Start the Db2 command line client using:

```
db2
```

Open a connection to your personal database, where you can practice SQL, experiment, and test SQL queries for assignments:

```
connect to cd2db3
```

After connecting, you can run any SQL queries. To see the list of tables in your database, run the SQL query:

```
LIST TABLES 
```

Use `quit` to end the command line client, and `exit` to logout of the SSH connection

## Uploading your own datasets

Copy the file to the cs2db3.cas.mcmaster.ca server:  
```
# copies the file named filenameA from your local device to the cs2db3 server

# filenameA will be copied to your home folder ~ in the cs2db3 server and name the copy filenameB
scp filenameA linc94@cs2db3.cas.mcmaster.ca~/filenameB
```

login to cs2db3 server via SSH:

```
ssh linc94@cs2db3.cas.mcmaster.ca
```

execute the statements in the file:

```
db2 -tvf filenameB
```
- `db2`: starts the Db2 command line client
- `filename`: read from an input file *filename* and execute statements from that file
- `-t` sets the statement termination character to `;`
    - combined with `-f` parameter, this allows you to write an easy to read human formatted file with all SQL queries that properly execute on the server
- `-v` runs in verbose mode, which will print out each statement
    - combined with `-f` parameter wil give you more feedback when executing a file full of statements

> Note: `connect to 2db3;` is used to check that you're connected to the correct database