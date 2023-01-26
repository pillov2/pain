#code examples (with some additions) from Graphical Data Analysis with R by Unwin


library(ggplot2)
library("gridExtra")
library("GGally")
library("ggthemes")
library(KernSmooth)
library("gridExtra")
library("GDAdata")
library("reshape")
library("vcd")
library("VGAMdata")


# Iris data
data(iris)

#pairs plot
ggpairs(iris, aes(colour=Species, alpha=0.4))     

      
#parallel co-ordinates plot
ggparcoord(iris, columns=1:4, groupColumn="Species")

#compare boxplots
#Sepal Width
a <- ggplot(iris, aes("Boxplot for all", Sepal.Width)) +
            xlab("")  + geom_boxplot() +
            scale_x_discrete(breaks=NULL) 
b <- ggplot(iris, aes(Species, Sepal.Width)) + 
            geom_boxplot() +  xlab("")
grid.arrange(a, b, nrow=1, widths=c(1,2))

#Petal Width
a <- ggplot(iris, aes("Boxplot for all", Petal.Width)) +
            xlab("")  + geom_boxplot() +
            scale_x_discrete(breaks=NULL) 
b <- ggplot(iris, aes(Species, Petal.Width)) + 
            geom_boxplot() +  xlab("")
grid.arrange(a, b, nrow=1, widths=c(1,2))


# Basic violin plot
vi <- ggplot(iris, aes(x=Species, y=Sepal.Width)) + 
  geom_violin()
vi
# Rotate the violin plot
vi + coord_flip()
# Set trim argument to FALSE
ggplot(iris, aes(x=Species, y=Sepal.Width)) + 
  geom_violin(trim=FALSE)
??geom_violin

#Add median and interquartile range
vi + geom_boxplot(width=0.1)


# Add dot plot
vi + geom_dotplot(binaxis='y', stackdir='center', dotsize=.5)

#colour by Species
vi<-ggplot(iris, aes(x=Species, y=Sepal.Width, fill=Species)) +
  geom_violin(trim=FALSE)
vi

# my favourite representation
vinew <- ggplot(iris, aes(x=Species, y=Sepal.Width, fill=Species)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="                Plot of Sepal Width by Species",x="Species", y = "Sepal Width")
vinew + theme_classic()

#save image
#dev.print(device=postscript, "image.eps", onefile=FALSE, horizontal=FALSE)



# Coffee data
data(coffee, package="pgmm")

#I want to use variety names, not number representation, in my graphs
coffee <- within(coffee, Type <- ifelse(Variety==1,"Arabica", "Robusta"))

#make the variable names shorter so the graphs look clearer
names(coffee) <- abbreviate(names(coffee), 8)

#pairs plot
ggpairs(coffee[,-c(1,2)], aes(colour=Type, alpha=0.4))  

#manually change variable name         
names(coffee)[6]<-"Ph"

#pairs plot
ggpairs(coffee[,-c(1,2)], aes(colour=Type, alpha=0.4))   

#reproduce the cover of Unwins book        
a <- ggplot(coffee, aes(x=Type)) + geom_bar(aes(fill=Type)) +
            scale_fill_manual(values = c("grey70", "red")) +
            guides(fill=FALSE) + ylab("")
b <- ggplot(coffee, aes(x=Fat, y=Caffine, colour=Type)) +
            geom_point(size=2) +
            scale_colour_manual(values = c("grey70", "red"))
c <- ggparcoord(coffee[order(coffee$Type),], columns=3:14,
                groupColumn="Type", scale="uniminmax") +
                xlab("") +  ylab("") +
                theme(legend.position = "none") +
                scale_colour_manual(values = c("grey","red")) +
                theme(axis.ticks.y = element_blank(),
                axis.text.y = element_blank())
                
grid.arrange(arrangeGrob(a, b, ncol=2, widths=c(1,2)), c, nrow=2)



