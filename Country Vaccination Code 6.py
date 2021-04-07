import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter, WeekdayLocator
from datetime import timedelta

vac = pd.read_csv(r"country_vaccinations.csv", usecols=['date', 'country', 'total_vaccinations'],
                  parse_dates=['date'])
countries = ['United States', 'Germany', 'United Kingdom', 'Israel', 'Ireland']
vac = vac[vac['country'].isin(countries)]
vac.fillna(value=0, inplace=True)
for index in range(len(countries)):print('countries:', countries[index])

