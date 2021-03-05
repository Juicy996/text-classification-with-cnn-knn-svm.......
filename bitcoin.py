import os, sys
import tensorflow as tf
import numpy as np
import pandas as pd

dataset = pd.read_csv("BTC_USD_2019-12-26-CoinDesk(1).csv",delimiter=",") 
print(dataset)
#print(dataset.shape)
