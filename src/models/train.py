import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from joblib import dump

from src.pipeline.pipeline import create_pipeline

def train_model (df):
    #Split the X and y
    X = df.drop('salary', axis=1)
    y = np.log(df['salary'])

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

    #create pipeline
    model = create_pipeline()

    #Train model
    model.fit(X_train, y_train)

    return model, X_test, y_test 

def save_model (model, path = "models/model.joblib"):
    dump(model, path)
