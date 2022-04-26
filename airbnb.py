"""
Created on Tue Apr 26 19:51:19 2022
@author: ashwini
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class airbnbData(BaseModel):
    guests: float
    bedrooms: float
    beds: float
    bathrooms: float 
    kitchen: float
    free_parking: float
    rating: float 
    City: float
    
class prediction(BaseModel):
    Airbnb_price_prediction: float
    
    