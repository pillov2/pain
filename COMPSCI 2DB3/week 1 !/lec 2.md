# Lecture 2 Notes

- Technically speaking: none of them are DBMS
- websites are not used to manage or access data, they are usually the ones using the data
- data analysis tools are used to manipulate the data but do not manage the data
- files and file systems are usually data and do not manage the data itself
  
Schema: description of the data:
- ex: a table; schema would describe the number of columns and rows in the table
- domain: type of vairable, int, string ex
- key is used to identify a whole section of data (represented by an underlined title [id])

Entity-Relationship data model
- kinda more visual compared to tables
- specify meaning ant not representation, ex: what a faculty is and what a course is 

Models
- rectangles are sets
- circles/ovals are attributes
- underlined values are keys
- instead of storing age, store birthdate, which is more general and easier to maintain. this is because you can derive someone's age through their birthday but you cannot derive their birthday from their age
- separate first name and last name becuase names can be very complex (???)
- students can enroll in classes: blue diamond rectangles represent a relationship between sets
- relationships are unique: a student cannot take a single course multiple times in this model
- relationships can also have attributes, such as year, but that does not change the fact that students can only take a single course
- 
