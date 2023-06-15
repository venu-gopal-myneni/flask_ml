# importing modules and packages
import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error


def read_csv(filename,target,split =0.3):
    """
        Read and split data
    """
    file_path = str(Path(__file__).parent.parent.joinpath("csv_data",filename))
    df = pd.read_csv(file_path)
    X = df.drop(target,axis=1)
    Y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=split, random_state=101)
    return X_train,X_test,y_train,y_test


def train_evaluate(X_train,X_test,y_train,y_test):
    # creating a regression model
    model = LinearRegression()

    # fitting the model
    model.fit(X_train, y_train)

    # making predictions
    predictions = model.predict(X_test)

    mse=mean_squared_error(y_test, predictions)
    mae=mean_absolute_error(y_test, predictions)

    # model evaluation
    print('mean_squared_error : ', mean_squared_error(y_test, predictions))
    print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
    return mse, mae

if __name__ == "__main__":

    filename= "real_estate.csv"
    target = 'Y house price of unit area'
    split =0.3
    X_train,X_test,y_train,y_test=read_csv(filename,target,split)
    mse, mae=train_evaluate(X_train,X_test,y_train,y_test)