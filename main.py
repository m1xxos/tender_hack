import pandas as pd

df_state = pd.read_csv('/Users/alaykhunov/Downloads/data/contracts.csv', sep=';')

df_state.drop_duplicates(subset='c', keep='first', inplace=True, ignore_index=False)
df_state.dropna(axis=0, how='any', subset='contract_reg_number', inplace=True)

df_state.to_csv('/Users/alaykhunov/Downloads/data/contracts-2.csv')
