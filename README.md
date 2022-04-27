# airbnb_price_prediction-using-FastAPI-Azure-deployment
capstone project for airbnb price prediction 

#To initiate the machine learning model this create pickle file which will be used to predict prices
>> python model.py 

# To initiate the the Fast API
>> python app.py
#has used local host with port 8000
localhost:8000 in browser will open the app

could use localhost:8000/docs to input the details 

update startup command in azure webapp in App service -> Configuration -> General settings 
> gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:8000" --log-level debug app:app #8000 is the port to connect to 
   
   ![image](https://user-images.githubusercontent.com/30444433/165520737-44e93b3b-fc48-42d5-8eaf-66e92a67cae5.png)

After successfully deployed. Input given in post command

![image](https://user-images.githubusercontent.com/30444433/165520970-899a9d7a-cf8e-4bd3-829a-a45518767890.png)

The output of Airbnb predicted price.

![image](https://user-images.githubusercontent.com/30444433/165521178-babf3a14-b629-49f6-9fd6-7bc73737e048.png)
