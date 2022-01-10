import pandas as pd
import numpy as np
from django.conf import settings

class WaccPredictor:
    def __init__(self):
        pass

    def predict(self, interest_rate, loan_size, value):

        loan_cost = interest_rate*(loan_size/value)
        eq_cost = 0.8*0.1*((value-loan_size)/value)
        return loan_cost+eq_cost
