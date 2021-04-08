import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

vac = pd.read_csv(r"country_vaccinations.csv")
vac.fillna(value=0, inplace=True)

plt.figure(figsize=(12, 7))
order_data = vac.groupby("country").total_vaccinations.agg("max").sort_values(ascending = False)
order_data[order_data> 1250000].plot(kind = "bar")
plt.ylabel("Total No of people vaccinated()")
plt.title("Country")
plt.show()