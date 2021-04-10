import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
vac = pd.read_csv(r"country_vaccinations.csv")

plt.figure(figsize=(16,7))
grp = ['country', 'total_vaccinations', 'iso_code', 'vaccines']
vacc_no = vac[grp].groupby('vaccines').max().sort_values('total_vaccinations', ascending=False).dropna(subset=['total_vaccinations'])


plt.bar(vacc_no.index, vacc_no.total_vaccinations, color ='m')

plt.title('Various categories of COVID-19 vaccines offered')
plt.xticks(rotation = 90)
plt.ylabel('Number vaccinated per 10 Million)')
plt.xlabel('Vaccines')
plt.show();