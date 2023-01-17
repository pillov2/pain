# most code with edits from R in Action by Kabacoff and Graphical Data Analysis with R by Unwin.


#note:  rm(list=ls()) clears the memory

##### Slide 2 #####
#let's make a graph using ggplot2
library(ggplot2)
library(mosaicData)
theme_set(theme_bw())

#what I always do first with a dataset
?CPS85
str(CPS85)
head(CPS85)

#compare this empty graph... 
ggplot(data = CPS85, mapping = aes(x = exper, y = wage))

#to this graph with data points
ggplot(data = CPS85, mapping = aes(x = exper, y = wage)) + geom_point()

#There is one high wage outlier. Let's only use wages that are less than 40.
CPS85 <- CPS85[CPS85$wage < 40,]

ggplot(data = CPS85, mapping = aes(x = exper, y = wage)) + geom_point()

#Change the apperance
??ggplot2

#alpha = transparancy
ggplot(data = CPS85, mapping = aes(x = exper, y = wage)) +
geom_point(color = "cornflowerblue", alpha = .7, size = 3)

#fit a regression line (lm=linear model) to our graph
ggplot(data = CPS85, mapping = aes(x = exper, y = wage)) +
geom_point(color = "cornflowerblue", alpha = .7, size = 3) +
geom_smooth(method = "lm")

#Lets seperate our data by sex. We will identify male and female data points using color, shape and linetype. se = FALSE suppresses the confidence intervals.
myplot<- ggplot(data = CPS85, mapping = aes(x = exper, y = wage,
color = sex, shape = sex, linetype = sex)) +
geom_point(alpha = .7, size = 3) +
geom_smooth(method = "lm", se = FALSE, size = 1.5)

#save the plot to your current working directory. You can use pdf, jpeg, tiff, png, svg, wmf
ggsave(file="myplot.pdf")

##### Slide 3 #####
#Bar Charts
library(vcd)
library(ggplot2)

#look at your dataset
?Arthritis
str(Arthritis)
head(Arthritis)

#Simple bar chart
ggplot(Arthritis, aes(x=Improved)) + geom_bar() + 
labs(title="Simple Bar chart", x="Improvement", y="Frequency") 

#Horizontal bar chart
ggplot(Arthritis, aes(x=Improved)) + geom_bar() + 
labs(title="Horizontal Bar chart", x="Improvement", y="Frequency") + 
coord_flip() 

#Stacked bar chart
ggplot(Arthritis, aes(x=Treatment, fill=Improved)) + geom_bar(position = "stack") + 
labs(title="Stacked Bar chart", x="Treatment", y="Frequency") 

#Grouped bar chart
ggplot(Arthritis, aes(x=Treatment, fill=Improved)) + geom_bar(position = "dodge") + 
labs(title="Grouped Bar chart", x="Treatment", y="Frequency") 

#Filled bar chart, rescaled so the height of each bar is 1 and the segment heights represent proportions.
ggplot(Arthritis, aes(x=Treatment, fill=Improved)) + geom_bar(position = "fill") + 
labs(title="Stacked Bar chart", x="Treatment", y="Frequency") 

#generally, ggplot2 uses "fill" to specify the color of areas (e.g bars, pie slices, boxes),
#and "color" for geometric objects without area (e.g. lines, points, and borders)

ggplot(Arthritis, aes(x=Improved)) + geom_bar(fill="gold", color="black") +
labs(title="Treatment Outcome")


##### The Titanic dataset 
library("gridExtra")

Titanic1 <- data.frame(Titanic)
head(Titanic1)
str(Titanic1)

#specify fill colours
p <- ggplot(Titanic1, aes(weight=Freq)) + ylab("") + ylim(0,2250)
c <- p + aes(Class) + geom_bar(fill="blue")
s <- p + aes(Sex) + geom_bar(fill="green")
a <- p + aes(Age) + geom_bar(fill="yellow")
sv <- p + aes(Survived) + geom_bar(fill="red")
grid.arrange(c, s, a, sv, nrow=1, widths=c(3, 2, 2, 2))

doubledecker(Survived ~ Sex, data = Titanic, gp = gpar(fill = c("grey", "red")))

doubledecker(Survived ~ Class, data = Titanic, gp = gpar(fill = c("grey", "red")))

doubledecker(Survived ~ Sex + Class, data = Titanic, gp = gpar(fill = c("grey", "red")))

