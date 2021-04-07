import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandasql import sqldf
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

plt.figure(figsize=(12, 7))
order_data = vac.groupby("country").total_vaccinations.agg("max").sort_values(ascending = False)
order_data[order_data> 20].plot(kind = "bar")
plt.ylabel("No of people vaccinated()")
plt.title("Country")
plt.show()