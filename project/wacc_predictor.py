import pandas as pd
import numpy as np
from django.conf import settings
from project.constants import *


class WaccPredictor:
    def predict(self, interest_rate, loan_size, value):
        loan_cost = interest_rate * (loan_size / value)
        eq_cost = (1-tax_rate) * stock_return * ((value - loan_size) / value)
        return loan_cost + eq_cost
