"""
This is a boilerplate pipeline 'general_data_processing'
generated using Kedro 0.18.3
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#  The dataset is ready so we do not have many processing tasks

def general_processing(df):
    df.drop(columns=['Unnamed: 0', 'UTC'], inplace=True)
    
    y = df['Fire Alarm']
    x = df.drop('Fire Alarm', axis = 1)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 10)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return X_train, X_test, y_train, y_test