"""Machine learning functions"""
# Import the appropriate estimator class from Scikit-Learn
from sklearn.linear_model import LinearRegression
from datetime import datetime



from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .models import Pop_Table
import simplejson as json



# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

router = APIRouter()



# this is for a prediction that was predicted "APRIORI"  
# (AKA ahead of time and stored in db up to the year 2022)
@router.get('/predict_population')
async def predict(year, city_state):
    """
    Request URL
    http://127.0.0.1:8000/predict_population?year=2012&city_state=Newark%2C%20New%20Jersey
    
    
    Predict population in Newark, New Jersey.
    {
        "city_state": "Newark, New Jersey",
        "year": 2012
    }

    """
    
    return {
            "population": 276478,
            "city_state": city_state,
            "year": year,
            "id_num": 19634
            }


# This is for the combined recommendation model
@router.get('/recommend')
async def recommendatio_model(crime_rate, rental_rate, population):
    """
    Request URL
    http://127.0.0.1:8000/recommend?crime_rate=1.0&rental_rate=10000&population=30000

    Predict population in Newark, New Jersey.
    {
        "crime_rate" : 1.0
        "rental_rate" : 10000
        "population" : 30000
    }

    """
    
    results = [
                {
                    "city_state" : "New York, New York",
                    "crime_rate" : 2.2,
                    "rental_rate" : 10000,
                    "population" : 250000,
                },
                                {
                    "city_state" : "New York, New York",
                    "crime_rate" : 2.2,
                    "rental_rate" : 10000,
                    "population" : 250000,
                },
                                {
                    "city_state" : "New York, New York",
                    "crime_rate" : 2.2,
                    "rental_rate" : 10000,
                    "population" : 250000,
                },
                                {
                    "city_state" : "New York, New York",
                    "crime_rate" : 2.2,
                    "rental_rate" : 10000,
                    "population" : 250000,
                },
                                {
                    "city_state" : "New York, New York",
                    "crime_rate" : 2.2,
                    "rental_rate" : 10000,
                    "population" : 250000,
                },
                                {
                    "city_state" : "New York, New York",
                    "crime_rate" : 2.2,
                    "rental_rate" : 10000,
                    "population" : 250000,
                },
            ]
    return results