# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:56:48 2022

@author: w0454974
"""

import pandas as pd

data = pd.read_csv("output/input.csv")

fig = data.age.plot.hist().get_figure()
fig.savefig("output/descriptive.png")