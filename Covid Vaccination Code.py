import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

vac = pd.read_csv(r"country_vaccinations.csv")

print(vac.columns)
print(vac.head())
print(vac.info())
vac.fillna(value=0, inplace=True)
print(vac.isnull().sum())







