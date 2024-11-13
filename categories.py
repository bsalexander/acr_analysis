
import pandas as pd

df = pd.read_csv('data/acr_ac_scenarios.csv')
unique_values = df.iloc[:, 0].unique()
print(unique_values)
