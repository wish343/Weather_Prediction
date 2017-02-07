totalData <- read.csv('C:/Users/wIsh/Desktop/Big Data/Project/analyzed.csv')
set.seed(350)
index <- sample(1:nrow(totalData), size<-0.75*nrow(totalData))
data_testing<- totalData[-index,]
res <- gain.ratio(FRSHTT~., data_testing)

library(randomForest)

lrModel <- lm(FRSHTT~.,data = data_training)
summary(lrModel)
#Creating Correlation matrix for complete data
corelation_matrix <- cor(totalData)
library('FSelector')
res <- gain.ratio(FRSHTT~., data_testing)
data_training<- totalData[index,]

#Creating classification tree
install.packages("rpart")
library(rpart)
frmla = FRSHTT ~ .

fit = rpart(frmla,  method = "class", data=totalData)

printcp(fit) # display the results
plotcp(fit) # visualize cross-validation results
summary(fit) # detailed summary of splits

# plot tree
plot(fit, uniform=TRUE, main="Classification Tree")
text(fit, use.n=TRUE, all=TRUE, cex=0.6)
