import numpy as np
import pandas as pd
from sklearn import model_selection as ms
import os
from config import numberOfFolds

if __name__ == "__main__":

    # Reading the dataset
    df = pd.read_csv("data/final_train.csv")

    # Creating KFold Object
    kfold = ms.StratifiedKFold(n_splits=numberOfFolds, shuffle=False)

    # Creating a Fold column
    df['Fold'] = -1
    # Shuffling the dataset
    df.sample(frac=1).reset_index(drop=True)

    # Seperate training and validation data
    for fold, (train_idx, val_idx) in enumerate(kfold.split(X=df, y=df["DEATH_EVENT"])):
        # print(len(train_idx), len(val_idx))
        df.loc[val_idx, 'Fold'] = fold

    # Save new fold dataset
    df.to_csv('data/train_folds.csv', index=False)
