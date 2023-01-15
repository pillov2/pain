# Lecture 3 Notes

- no standard solution that works in all cases because there are too many cases to cover

- can have multiple attributes combined in a "key"

- relationships that have attributes
    - data will only be defined by its relationship, independent of the attributes
        - claudia took databses in 2020, even if she wanted to retake the course in a different year, she wouldn't be able to because the pair(claudia, databases) is already in the database, again, independent of the attribute (year)

- a single arrow creates a key constraint, meaning that they can only have a maximum of one of the relationship
- a single rounded arrow creates another key constraint, meaning that they must have only one relationship
- a bolded line means that the entity will always have the relationship

### Weak Entities
- ex: 2DB3 is owned by COMPSCI
- this class's first assignment is owned by 2DB3 COMPSCI
- weak keys are represented by dotted lines
- round arrows are needed because they MUST be related to their 'owner'
