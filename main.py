# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    age : int
    sex : int
    bloodpressure : float
    cholesterol : int
    diabetes : int
    smoking : int    

# loading the saved model
model = pickle.load(open('heartdisease_model.pkl','rb'))


@app.post('/cardiac_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    bp = input_dictionary['bloodpressure']
    ch = input_dictionary['cholesterol']
    db = input_dictionary['diabetes']
    smk = input_dictionary['smoking']



    input_list = [age, sex, bp, ch, db, smk]
    
    prediction = model.predict([input_list])
    
    if prediction[0] == 0:
        return 'There is no risk of cardiovascular disease in the next ten years.'
    
    else:
        return 'There is high risk of cardiovascular disease in the next ten years.'


