from numpy import array
from numpy import hstack
import pandas as pd
import numpy as np
from sklearn import preprocessing
from datetime import datetime
import os
from math import sqrt

from keras.models import Sequential, load_model
from keras.metrics import mean_squared_error
from keras.layers import Flatten, BatchNormalization, Dropout, LocallyConnected2D, LeakyReLU, ReLU, Dense
from keras.layers.convolutional import Conv2D
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard

import plotly.graph_objects as go
import matplotlib.pyplot as plt

turbine = 'T03'  # ["T22","T34","T54","T01","T02","T03","T09","T40"]
model_name = 'CNN2'
version = 5
split = 0.025
n_steps = 144

n_features = 4

# Select feature list for model
if model_name == "CNN1":
    features = ['Ambient_Temperature', 'Active_Power', 'Wind_Speed', 'Generator_RPM', 'Generator_Bearing_Tempeature']
elif model_name == "CNN2":
    features = ['Ambient_Temperature', 'Active_Power', 'Wind_Speed', 'Generator_RPM', 'Gear_Oil_Tempeature']
