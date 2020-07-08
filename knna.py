import pandas as pd
import numpy as np
import pandas_profiling as pp
df=pd.read_csv("/storage/emulated/0/project/admission1.csv")
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.shape)
print(df.info)
print(df.describe())
Profile = pp.ProfileReport(df)
Profile.to_file("/storage/emulated/0/project/report1.html")
df=df.drop("Research",axis=1)
print(df.shape)
print(df.head())
from sklearn.model_selection import train_test_split
y=df["Chance_of_Admit"]
X=df.drop('Chance_of_Admit',axis=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
from sklearn.metrics import confusion_matrix,accuracy_score
conf_mat = confusion_matrix(y_test,y_pred)
print(conf_mat)
acc_score = accuracy_score(y_test,y_pred)
print(acc_score)
new_parameters=[[340,120,4.5,5.0,5.0,9.8,1]]
Chance_of_Admit_predicted=knn.predict(new_parameters)
print(Chance_of_Admit_predicted)