import pandas as pd
import numpy as np
import pandas_profiling as pp
df=pd.read_csv("/Storage/emulated/0/project/admission1.csv")
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.shape)
print(df.info)
print(df.describe())
Profile = pp.ProfileReport(df)
Profile.to_file("/Storage/emulated/0/project/report1.html")
df=df.drop("Research",axis=1)
print(df.shape)
print(df.head())
y=df[['Chance_of_Admit']]
X=df.drop('Chance_of_Admit',axis=1)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
print(model.fit(X_train,y_train))
y_pred = model.predict(X_test)
print(y_pred)
print(y_test)
from sklearn.metrics import accuracy_score,confusion_matrix
conf_mat = confusion_matrix(y_pred,y_test)
acc_score = accuracy_score(y_pred,y_test)
print(conf_mat)
print(acc_score)
new_parameters=[[340,120,4.5,5.0,5.0,9.8,1]]
Chance_of_Admit_predicted=model.predict(new_parameters)
print(Chance_of_Admit_predicted)