from sklearn.datasets import load_digits
import numpy as np
import pandas as pd


digits = load_digits()
data = digits.data
labels = digits.target

split_index = len(data) // 2 #size of data and labels arrays are identical
training_data = data[:split_index]
testing_data = data[split_index:]

training_labels = labels[:split_index]
testing_data = labels[split_index:]