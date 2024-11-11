from fastapi import FastAPI, Query
import pandas as pd
import json

app = FastAPI()

df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv")


@app.get("/api/flights/search")

def get_flights(type: str = Query(), 
                code: str = Query()):
    
    if type == "dep":
        flights = df[df["departure_airport_code"] == code]
    elif type == "arr":
        flights = df[df["arrival_airport_code"] == code]
    else:
        return {}

    #departure code
    json_flights = flights.to_json(orient="records")

    #arrival code

    return json.loads(json_flights)


    
    