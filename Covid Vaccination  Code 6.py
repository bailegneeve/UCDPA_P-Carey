import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
vac = pd.read_csv(r"country_vaccinations.csv")

plt.figure(figsize=(15,6))
grp = ['country', 'total_vaccinations', 'iso_code', 'vaccines']
vacnum = vac[grp].groupby('vaccines').max().sort_values('total_vaccinations', ascending=False).dropna(subset=['total_vaccinations'])


plt.bar(vacnum.index, vacnum.total_vaccinations, color ='g')

plt.title('Categories of COVID-19 vaccines offered')
plt.xticks(rotation = 90)
plt.ylabel('Number vaccinated per 10 Million)')
plt.xlabel('Vaccines')
plt.show();