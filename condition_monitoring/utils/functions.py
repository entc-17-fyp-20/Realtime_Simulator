from numpy import array
import pandas as pd
from datetime import datetime
import numpy as np


# split a multivariate sequence into samples
def split_sequences(sequences, n_steps):
    X, y = list(), list()
    for i in range(len(sequences)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the dataset
        if end_ix > len(sequences):
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix - 1, -1]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


def maxmin(x, ftr, statistics):
    stat = statistics.loc[ftr, :]
    x = (x - stat['min']) / (stat['max'] - stat['min'])
    return x


def get_statistics():
    path = 'data/T1-T3_stats.csv'
    statistics = pd.read_csv(path)
    statistics = statistics.set_index(statistics['Unnamed: 0'])
    statistics.drop('Unnamed: 0', inplace=True, axis=1)  # max-min input
    return statistics


def apply_maxmin(df, features, statistics):
    df_time = pd.DataFrame(df["Date_Time"], columns=['Date_Time'])
    df.drop("Date_Time", axis='columns', inplace=True)

    for ftr in features:
        df[ftr] = df[ftr].apply(lambda row: maxmin(row, ftr, statistics))

    df["Date_Time"] = df_time["Date_Time"]
    df = df.set_index(df['Date_Time'])
    return df


def get_split_index(df):
    datatime_format = '%Y-%m-%d %H:%M:%S'
    split_index = [df['Date_Time'][0]];
    for i in range(0, len(df['Date_Time']) - 1):
        current_time = df['Date_Time'][i]
        following_time = df['Date_Time'][i + 1]
        time_gap = datetime.strptime(following_time, datatime_format) - datetime.strptime(current_time, datatime_format)
        if time_gap.total_seconds() != 600:
            split_index.append(current_time)
            split_index.append(following_time)
    split_index.append(df['Date_Time'][len(df['Date_Time']) - 1])
    return split_index


def apply_split_index(df, l, split_index, n_steps=144):
    # l = list of features
    y_concat_test, X_concat_test = [], []
    for i in range(0, len(split_index), 2):
        dfx = df[split_index[i]:split_index[i + 1]]
        if len(dfx) >= n_steps:
            dfx = dfx[l]
            dfx = dfx.to_numpy()
            # convert into input/output
            X, y = split_sequences(dfx, n_steps)
            X_concat_test.append(X)
            y_concat_test.append(y)

    X_concat_test = tuple(X_concat_test)
    y_concat_test = tuple(y_concat_test)

    # Concatenating datasets
    X_test = np.concatenate(X_concat_test)
    y_test = np.concatenate(y_concat_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], X_test.shape[2], 1))

    return X_test, y_test


def add_datetime(df, df_final, split_index, n_steps=144):
    frames = []

    for i in range(0, len(split_index), 2):
        dfx = df[split_index[i]:split_index[i + 1]]
        frames.append(dfx.iloc[n_steps - 1:, :])

    test = pd.concat(frames)
    test.drop("Date_Time", axis='columns', inplace=True)
    test = test.reset_index()
    df_final["Date_Time"] = test["Date_Time"]

    return df_final
