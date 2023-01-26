# from R in Action by Kabacoff

#note:  rm(list=ls()) clears the memory

#Age (months) and corresponding Weight (Kg) of 10 babies

#Age and Weight are entered as vectors using the function c()
#c() combines its arguments into a vector or list
age <- c(1,3,5,2,11,9,3,9,12,3)
weight <- c(4.4,5.3,7.2,5.2,8.5,7.3,6.0,10.4,10.2,6.1)

#calculate the mean and standard deviation of the weights
mean(weight)

sd(weight)

#calculate the correlation between age and weight
cor(age,weight)

# basic scatter plot of age against weight
plot(age,weight)


#################################

#lots of background reading
help.start()

#install package vcd, for visualizing categorical data#install.packages("vcd")

#about the package
help(package="vcd")

#you need to load the package for this current coding seessionlibrary(vcd)

#information about the "Arthritis dataset", which is housed in the vcd package
help(Arthritis)

#print out the entries in the datasetArthritis

#create a contingency table using "xtabs"
#the cross-classifying variables are separated by + 
#only looking at Female patients
art <- xtabs(~ Treatment + Improved, data = Arthritis, subset = Sex == "Female")

#print your result
art

