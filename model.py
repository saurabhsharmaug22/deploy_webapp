# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:27:16 2020

@author: HP
"""


from pycaret.regression import *
from pycaret.datasets import get_data

data = get_data('insurance')

r2 = setup(data, target='charges', session_id= 123,
           normalize=True,
           polynomial_features=True, trigonometry_features=True,
           feature_interaction=True,
           bin_numeric_features=['age', 'bmi'])

lr = create_model('lr')

plot_model(lr, plot='residuals')

save_model(lr, model_name='deployement_04052020')

