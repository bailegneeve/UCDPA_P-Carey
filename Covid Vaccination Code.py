import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
vac = pd.read_csv(r"/Users/pc/Downloads/country_vaccinations.csv")
print(vac.head())
print(vac.info())

vac.fillna(0,inplace=True)
vac.isnull().sum()

