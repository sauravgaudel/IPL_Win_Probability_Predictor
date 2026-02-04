from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pickle
import pandas as pd

from .schemas.input import Input
from .cors import add_cors

with open("Model/pipe.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI()
add_cors(app)  

@app.get('/')
def home():
    return {'Hello':'It is Home Page of the IPL Win Probability API'}   

@app.post('/predict')
def Predict(data: Input):

    input_df = pd.DataFrame([{
        'batting_team': data.batting_team,
        'bowling_team': data.bowling_team,
        'city': data.city,
        'runs_left': data.runs_left,
        'balls_left': data.balls_left,
        'wickets_left': data.wickets_left,
        'total_runs_x': data.total_run_x,
        'CRR': data.CRR,
        'RRR': data.RRR
    }])

    if data.batting_team == data.bowling_team:
        raise HTTPException(
            status_code=400, 
            detail="Batting team and Bowling team cannot be the same."
        )

    prediction = model.predict_proba(input_df)[0]

    return JSONResponse(status_code=200, content={'Probability': {
        'batting_team': round(prediction[1]*100, 2),
        'bowling_team': round(prediction[0]*100, 2)
    }})
