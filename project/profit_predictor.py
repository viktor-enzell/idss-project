import pandas as pd
import numpy as np
from django.conf import settings
from project.constants import *
import matplotlib.pyplot as plt


class ProfitPredictor:
    def predict(self, interest_rate, loan_size, value, price, wacc, rent):
        loan_cost = interest_rate * loan_size
        own_capital = price - loan_size
        fixed_cost = value - price
        yearly_earnings = utility_rate * rent * 365

        years = 10
        x = np.linspace(0, years, 1000)

        zero_line = x * 0
        y = (x * yearly_earnings - x * loan_cost) + (np.power(1.05, x) - 1) * value + fixed_cost

        wacc_line = (np.power(1 + wacc, x)-1)*price
        
        stock_line = (np.power(1 + stock_return, x)-1)*price
        upper_stock_line = (np.power(1.12, x)-1)*price
        lower_stock_line = (np.power(0.9, x)-1)*price
        
        plt.clf()
        plt.plot(x, wacc_line, color = 'red', label = 'Cost of Capital')
        plt.plot(x, stock_line, color = 'blue', label = 'Stock Return')
        plt.plot(x, y, color = 'green', label = 'Realestate Return')
        plt.fill_between(x,upper_stock_line, lower_stock_line, color = 'lightblue', label = 'Stock Return Bounds')
        plt.plot(x, zero_line, color = 'black', linewidth=1)
        plt.ylabel('€ Return')
        plt.xlabel('Year')
        plt.xlim([0, years])
        plt.tight_layout()
        plt.legend()
        plt.savefig('static/tmp.png') 
