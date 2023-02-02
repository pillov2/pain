install.packages("pgmm")
install.packages("tidyverse")
install.packages("vcd")

#Slide 2
library(ggplot2)
library(vcd)
library(pgmm)

#coffee data
data(coffee, package = "pgmm")

#use the "str" command to examine the data
head(coffee)
str(coffee)

#check for missing values
is.na(coffee)

#Slide 3

#barchart of countries
box1 <- ggplot(coffee, aes(x = Country)) + geom_bar() + theme(axis.text.x = element_text(angle = 65, vjust = 0.6))
box1

#barchart of variety
box2 <- ggplot(coffee, aes(factor(Variety))) + geom_bar()
box2

#mosaic plot of variety against country
#basic mosaic plot
a <- mosaic(Variety ~ Country, data = coffee)
a

b <- mosaic(Variety ~ Country, data = coffee, labeling = vcd :: labeling_border(rot_labels = c(0,45)))
b

#Distribution of the variables
boxplot(coffee[,3:14])

#scaled
boxplot(scale(coffee[,3:14]))

#scatterplot (pairs plot) of the continuous variables
pairs(coffee[,3:14])
