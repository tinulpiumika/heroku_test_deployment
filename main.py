# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:36:48 2022

@author: siddhardhan
"""

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

# class model_input(BaseModel):
#     Pregnancies : int
#     Glucose : int
#     BloodPressure : int
#     SkinThickness : int
#     Insulin : int
#     BMI : float
#     DiabetesPedigreeFunction :  float
#     Age : int
    

# loading the saved model
#diabetes_model = pickle.load(open('diabetes_model.sav','rb'))


@app.post('/diabetes_prediction')
def diabetes_pred():
    return "Hello World"


