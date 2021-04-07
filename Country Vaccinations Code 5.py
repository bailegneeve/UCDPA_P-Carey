import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
vac = pd.read_csv(r"country_vaccinations.csv")
daily = vac.groupby('country').total_vaccinations.agg("max").sort_values(ascending=False)

daily_a = daily.dropna(axis='rows').reset_index()

plt.figure(figsize=(15, 6))
plt.title('Top 12 best performing countries in daily vaccinations')
sns.barplot(x=daily_a.country[0:12], y=daily_a.total_vaccinations[0:12])
plt.xlabel(' ')
plt.ylabel('Daily vaccinations (in millions)');
plt.show()