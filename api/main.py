from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction
import pandas as pd

app = FastAPI()

class FeaturesInput(BaseModel):
    ApprovalDate: str
    Term: int
    NoEmp: int
    FranchiseCode: str
    ApprovalFY: int
    Naics: str
    NewExist: str
    LowDoc: str
    GrAppv: int
    CreateJob: int
    RetainedJob: int
    UrbanRural: str
    RevLineCr: str

class PredictionOutput(BaseModel):
    prediction : int

model = load_model()

@app.post('/predict', response_model=PredictionOutput)
def prediction_root(feature_input: FeaturesInput):
    data_dict = feature_input.dict()
    input_df = pd.DataFrame([data_dict])
    prediction_final = model.predict(input_df)
    

    
    return PredictionOutput(prediction=int(prediction_final[0]))