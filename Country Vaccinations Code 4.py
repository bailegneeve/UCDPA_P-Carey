import matplotlib.pyplot as plt
import pandas as pd

vac = pd.read_csv(r"country_vaccinations.csv",usecols=['date', 'country', 'total_vaccinations'],
parse_dates=['date'])
countries = ['United States', 'Germany', 'United Kingdom', 'Israel', 'Ireland']
vac = vac[vac['country'].isin(countries)]
vac.fillna(value=0, inplace=True)



plt.figure(figsize=(12, 7))
order_data = vac.groupby("country").total_vaccinations.agg("max").sort_values(ascending = False)
order_data[order_data> 20].plot(kind = "bar")
plt.ylabel("No of people Vaccinated()")
plt.title("Country")
plt.show()

