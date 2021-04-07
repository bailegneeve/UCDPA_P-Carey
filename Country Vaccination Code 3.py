import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandasql import sqldf
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

vac = pd.read_csv(r"country_vaccinations.csv")


vac.fillna(value=0, inplace=True)

cols = ['country', 'total_vaccinations', 'iso_code', 'vaccines','total_vaccinations_per_hundred']
vacc_amount = vac[cols].groupby('country').max().sort_values('total_vaccinations_per_hundred', ascending=False).dropna(subset=['total_vaccinations_per_hundred'])
vacc_amount = vacc_amount.iloc[:10]

vacc_amount = vacc_amount.sort_values('total_vaccinations_per_hundred', ascending=False)

plt.figure(figsize=(9, 15))
sns.barplot(vacc_amount.index, vacc_amount.total_vaccinations_per_hundred, color = 'g')
plt.ylabel('Number of vaccinated people per hundred')
plt.xlabel('Countries')
plt.show()

