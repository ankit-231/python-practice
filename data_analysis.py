import pandas as pd 

datafile = r'C:\Users\Lenovo\Downloads\sums\data analysis\dataset.csv'
df = pd.read_csv(datafile)

# display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# extract columns relevant to Cardiovascular Disease only
df = df[df['Topic'] == 'Cardiovascular Disease']

df.groupby('StratificationCategoryID1')['DataValue'].describe()

print(df[df['StratificationCategoryID1'] == 'OVERALL'])