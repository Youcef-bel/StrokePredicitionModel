import numpy as np
import pickle
import steamlit as st

model = pickle.load(open('clf.sav', 'rb'))
