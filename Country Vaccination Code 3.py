import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandasql import sqldf
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

vac = pd.read_csv(r"country_vaccinations.csv")


print(vac.head())
print(vac.info())
vac.fillna(value=0, inplace=True)
print(vac.isnull().sum())
print(sqldf("""
select country,max(people_vaccinated_per_hundred) as reach
from vac
group by country 
order by reach desc"""))
cols = ['country', 'total_vaccinations', 'iso_code', 'vaccines','total_vaccinations_per_hundred']
vacc_amount = vac[cols].groupby('country').max().sort_values('total_vaccinations', ascending=False).dropna(subset=['total_vaccinations'])
vacc_amount = vacc_amount.iloc[:10]

vacc_amount = vacc_amount.sort_values('total_vaccinations_per_hundred', ascending=False)

plt.figure(figsize=(9, 12))
sns.barplot(vacc_amount.index, vacc_amount.total_vaccinations_per_hundred, color = 'r')
plt.ylabel('Number of vaccinated people per hundred')
plt.xlabel('Countries')
plt.show()

