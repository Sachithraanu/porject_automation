import pandas as pd

df = pd.read_csv('beforward_bot/jan_toyota_1.csv')
df1 = df.dropna()
df1 = df1.drop_duplicates(subset='Ref', keep="last")
df1['Year'] = df1['Model'].str[:4]
df1['Name'] = df1['Model'].str[4:]
df1['Model_Name'] = df1['Name'].str[:15]
# df1[['Team', 'Conference']] = df1['Model_Name'].str.split(' ', 1, expand=True)
df1[['Team', 'Conference']] = df1['Model_Name'].series.str.split(' ', expand=True)
# df1['Model_Name','a','b','c','d'] = df1['Name'].str.split(' ', expand = True)
# df1['Name'].str.split(' ', expand = True)
# df1 = df1.join(df1['Name'].str.split(' ', 1, expand=True))
# df1 = df1['Name'].str.split(" ",expand = True)
# df1 = df1['Name'].str.split('\s{2,}', expand = True)
# new = df1["Name"].str.split(" ", n = 1, expand = True)
# df1.to_csv('PrePreocessedData.csv', index=False)
print(df1)


