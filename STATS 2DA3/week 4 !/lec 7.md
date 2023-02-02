# Lecture 7 Notes

## D3

- javascript allows web developers to produce client-side web 
    - i.e computations are occurring in the clients browser
- these applications tend to be very responsive to client interactions
- a popular javascript library is D3.js, which stands for Data Driven Documents
    - can make use of D3 without learning javascript by using the `htmlwidgets` package in `R`

## Plot.ly

- produces online dynamic data visualization
- based on a javascript library and is accessible in `R` through the `plotly` package
- can convert a `ggplot2` object into a `plotly` object by using the `ggplotly()` function

### Features

- after running `ggplotly()`, a graph is displayed in `R` or in a web browser
- functions supported include:
    - panning
    - zooming 
    - brushing (selected points are marked)
    - mouse-over annotations
        - additional information is displayed when a point is hovered over

## Data Tables

- `datatables(DT)` package converts data tables into a searchable interactive format
    - produces a search box and clickable sorting rows
    - also makes tables:
        - searchable
        - sortable
        - pageable