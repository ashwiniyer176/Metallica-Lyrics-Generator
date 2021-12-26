import joblib
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import tree
import os
import config


def returnXandY(data, label):
    '''
    Takes a dataset and its target column name and returns X and y
    '''
    X = data.drop(label, axis=1)
    y = data[label]
    return X, y


def run(fold, model, metric):
    """
    Takes in fold as an argument and runs the Decision Tree Model and prints Accuracy for the model per fold.
    """
    df = pd.read_csv("data/train_folds.csv")

    # Setting train data where Fold value != fold and validation where Fold value==fold
    df_train = df[df['Fold'] != fold].reset_index(drop=True)
    df_valid = df[df['Fold'] == fold].reset_index(drop=True)
    X_train, y_train = returnXandY(df_train, "DEATH_EVENT")
    X_val, y_val = returnXandY(df_valid, "DEATH_EVENT")

    classifier = model
    classifier.fit(X_train, y_train)
    preds = classifier.predict(X_val)
    accuracy = metric(y_val, preds)
    print(f"Fold={fold}  Accuracy={accuracy}")
    file = open(f"models/model_fold_{fold}.bin", "wb")
    joblib.dump(classifier, file)


if __name__ == "__main__":
    df = pd.read_csv("data/train_folds.csv")
    for k in df['Fold'].unique():
        run(fold=k, model=config.model, metric=config.metric)
