# Lecture 3 Notes

- ISA relationship is not like OOP
    - a person can be both a student and a personnel
    - to make ISA relationship restricted to one specialty only:
        - add a constraint to the documentation describing the ISA
            - ie. "in this diagram, you can only be ___ or ___
            - you must always have documentation when you have ISA relationships
- general notation for ISA relationships:
    - top of triangle points to superclass and the bottom points point to the specialties
    - you can have any number of specialties in an ISA relationship, they will all be at the bottom of the triangle
        - if you have like 20 or 30 specialties, you're either doing something very weird or you've done something very wrong
- use dotted lines to aggregate relationships and treat it as an entity
- attributes must be atomic values
    - you cannot have a key value pair as an attribute, you would have a key attribute and a value attribute
- entities can represent complex objects, and multiple attributes
    - you can have key value pairs

> notes for assignment 1:
> - will need entities, attribute, and relationships
> - might need a few weak entities, but definitely won't need to use aggregation

- a query language is a programming language
    - ask it to give you information regarding the data
