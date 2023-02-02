# most code with edits from R in Action by Kabacoff and Graphical Data Analysis with R by Unwin.

##### The Titanic dataset 
library(ggplot2)
library(vcd)
library("gridExtra")

Titanic1 <- data.frame(Titanic)
head(Titanic1)
str(Titanic1)


doubledecker(Survived ~ Sex, data = Titanic, gp = gpar(fill = c("grey", "red")))

doubledecker(Survived ~ Sex + Class, data = Titanic, gp = gpar(fill = c("grey", "red")))

doubledecker(Survived ~ Sex + Class + Age, data = Titanic, gp = gpar(fill = c("grey", "red")))

##### issue with labels #####
?mpg

ggplot(mpg, aes(x=model)) + geom_bar() +
labs(title="Car models in the mpg dataset", y="Frequency", x="")

#use a co-ordinate flip
ggplot(mpg, aes(x=model)) + geom_bar() +
labs(title="Car models in the mpg dataset", y="Frequency", x="") +
coord_flip()

#option b, angle the label and use a smaller font size
ggplot(mpg, aes(x=model)) + geom_bar() + labs(title="Model names in the mpg dataset",
y="Frequency", x="") +
theme(axis.text.x = element_text(angle = 45, hjust = 1, size=8))

##### Histograms #####
data(mpg)
?mpg

str(mpg)
head(mpg)

#only look at cars from the year 2008
cars2008 <- mpg[mpg$year == 2008, ]

#basic histogram
ggplot(cars2008, aes(x=hwy)) + geom_histogram() + 
labs(title="Default histogram") 

#colored histogram, 20 bins
ggplot(cars2008, aes(x=hwy)) + geom_histogram(bins=20, color="white", fill="steelblue") + 
labs(title="Colored histogram with 20 bins", x="City Miles Per Gallon", y="Frequency")

#hist. with percentages
# :: helps to access the exact function from a specific package
ggplot(cars2008, aes(x=hwy, y=..density..)) + geom_histogram(bins=20, color="white", fill="steelblue") + scale_y_continuous(labels=scales::percent) + labs(title="Histogram with percentages", y= "Percent", x="City Miles Per Gallon") 

#hist. with density curve 
ggplot(cars2008, aes(x=hwy, y=..density..)) + geom_histogram(bins=20, color="white", fill="steelblue") + scale_y_continuous(labels=scales::percent) + geom_density(color="red", size=1) + labs(title="Histogram with density curve", y="Percent" , x="City Miles Per Gallon")

