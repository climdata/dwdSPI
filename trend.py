import os
import sys
import math

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

from pathlib import Path

DATA_PATH = Path.cwd()


spiDF = pd.read_csv(DATA_PATH / 'csv' / 'spi_de.csv', delimiter=',') 

print(spiDF)

for month in [1,2,3,4,5,6,7,8,9,10,11,12]:
  subDF = spiDF[spiDF['month']==month].dropna()
  for spi in ['spi1','spi2','spi3','spi4','spi5','spi6','spi7','spi8','spi9','spi10','spi11','spi12']:
     X = np.array(subDF['year']).reshape(-1, 1)
     y = np.array(subDF[spi]).reshape(-1, 1)
     reg = LinearRegression().fit(X, y)
     print([month, spi, reg.score(X,y), reg.coef_]) 

