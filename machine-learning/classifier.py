import pandas as pd
import numpy as np
import sklearn as sk 
import sklearn.tree as skt
import sklearn.model_selection as skms
import sklearn.linear_model as sklm
import sklearn.neighbors as skn
import sklearn.ensemble as ske
import sklearn.naive_bayes as sknb
import sklearn.metrics as skm
import sklearn.preprocessing as skpp

data = pd.read_csv("mldata.csv")

data.fillna(value=data.mean(), inplace=True)

le = skpp.LabelEncoder()
data["COUNTRY"] = le.fit_transform(data["COUNTRY"])

x = pd.DataFrame(data, columns="COUNTRY,HDI,TC,TD,STI,POP,GDPCAP,AGE,POR,ARRVL,DPRT,SPI,ARI,DPI,TRI".split(','))
y = data["MRG"]
xTrain, xTest, yTrain, yTest = skms.train_test_split(x, y, test_size=0.1)
scaler = skpp.MinMaxScaler()
xTrain = scaler.fit_transform(xTrain)
xTest = scaler.fit_transform(xTest)

#Logistic Regression
regressor = sklm.LogisticRegression()
logReg = regressor.fit(xTrain, yTrain)
yPred = regressor.predict(xTest)
prediction = pd.DataFrame({"Actual":np.asarray(yTest).flatten(), "Prediction":yPred.flatten()})
print("LOGISTIC REGRESSION\n",prediction)
print(logReg.score(xTrain, yTrain))
print(logReg.score(xTest, yTest))


#K Neighbors Classifier 
knn = skn.KNeighborsClassifier()
KNeighbors = knn.fit(xTrain, yTrain)
yPred = knn.predict(xTest)
prediction = pd.DataFrame({"Actual":np.asarray(yTest).flatten(), "Prediction":yPred.flatten()})
print("K NEIGHBORS CLASSIFIER\n",prediction)
print(knn.score(xTrain, yTrain))
print(knn.score(xTest, yTest))

print(skms.cross_val_score(KNeighbors, xTrain, yTrain, cv=10, scoring="accuracy"))
print(skms.cross_val_score(KNeighbors, xTest, yTest, cv=10, scoring="accuracy"))
#prediction.to_csv("kNeighborsPrediction.csv")

#Gaussian Naive Bayes
gnb = sknb.GaussianNB()
gauss = gnb.fit(xTrain, yTrain)
yPred = gauss.predict(xTest)
prediction = pd.DataFrame({"Actual":np.asarray(yTest).flatten(), "Prediction":yPred.flatten()})
print("GAUSSIAN NB\n",prediction)
print(gnb.score(xTrain, yTrain))
print(gnb.score(xTest, yTest))
#prediction.to_csv("gaussianNBPrediction.csv")


