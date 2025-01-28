# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:12:21 2025

@author: 20224695
"""

import numpy as np
import matplotlib.pyplot as plt

attr_range = [1, 1, 1]
marg_range = [0.5 ,0.5, 0.5]
trans_range = [0, 1, 4]

cap = 10

value = 0
x_range = np.zeros((3))

for x in x_range:
    for attr in attr_range:
        for marg in marg_range:
            for trans in trans_range:
                value = value + attr*(x + trans)^(marg)
                
                
                