from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#load the dataset
data=pd.read_csv("airbnb.csv")

#Preprocessing

#data['Total_price']=data['Total_price'].str.replace(',', '').astype(int)
data[['Room_type', 'City','dummy','dummy']]=data['name'].str.split('in', expand=True)

#replace Room type which contains ‘Entire’ and hut (as it was expensive) with Entire home/apartment 
data['Room_type']= data['Room_type'].replace(to_replace =['Entire rental unit ', 'Entire home ', 'Entire apartment ','Entire serviced apartment ','Entire holiday home ', 'Entire loft ','Entire chalet ','Entire villa ','Hut '], 
                            value ="Entire home/apartment")

#Feature selection by dropping below column
data.drop(['Unnamed: 0', 'url', 'name', 'header','dummy','Actual_price per'], inplace = True, axis = 1) 
data.drop(['wifi' , 'Room_type','review'], inplace = True, axis = 1)
data['City'] = data['City'].astype("category").cat.codes # convert into categorical 
#data['Room'] = data['City'].astype("category").cat.codes # convert into categorical 

#train and test
 #, data['Total_price']
data_y =data.Total_price
data_x = data.drop(['Total_price'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3,random_state=42)

#using best model fit ElasticNet
model_enet = ElasticNet(alpha = 0.001)
model_enet.fit(X_train, y_train) 
pred_test_enet= model_enet.predict(X_test)

# 'guests', 'bedrooms', 'beds', 'bathrooms', 'kitchen','free-parking', 'rating', 'City'

import pickle
pickle_out = open("model_enet.pkl","wb")
pickle.dump(model_enet, pickle_out)
pickle_out.close()

model_enet.predict([[3,1,3,1,1,1,4,5]])