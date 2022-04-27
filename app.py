"""
Created on Tue Apr 26 19:51:19 2022
@author: ashwini
Using FastAPI to create 
"""
"""
Created on Tue Apr 26 19:51:19 2022
@author: ashwini
Using FastAPI to create 
"""
# 1. Library imports
import uvicorn
from fastapi import FastAPI, status
from airbnb import airbnbData,prediction
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model_enet.pkl","rb")
model_enet=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
# Data: 'guests', 'bedrooms', 'beds', 'bathrooms', 'kitchen','free-parking', 'rating', 'City'

@app.post('/predict',response_model=prediction , status_code= status.HTTP_200_OK )
async def predict_price(data:airbnbData):
    data = data.dict()
    guests=data['guests']
    bedrooms=data['bedrooms']
    beds=data['beds']
    bathrooms=data['bathrooms']
    kitchen=data['kitchen']
    free_parking=data['free_parking']
    rating=data['rating']
    City=data['City']
    print(model_enet.predict([[guests,bedrooms,beds,bathrooms,kitchen,free_parking,rating,City]]))
    prediction = model_enet.predict([[guests,bedrooms,beds,bathrooms,kitchen,free_parking,rating,City]])

    return {**data ,'Airbnb_price_prediction' : prediction }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1')#, port=8000)
    
#uvicorn app:app --reload
