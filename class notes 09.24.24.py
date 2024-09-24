import pandas as pd

filename= "./big-mac-full-index.csv"
df = pd.read_csv(filename)

# query = f"(iso_a3 == 'MEX')"
# #query = f"(iso_a3 =='MEX' and (date > 2019-01-01 and date < 2019-12-31))"
# mxn_df = df.query(query)

# #print(mxn_df)
# print(mxn_df['dollar_price'].min())
# print(mxn_df['dollar_price'].max())
# print(round(mxn_df)['dollar_price'].mean(),2)

# query =f"(iso_a3 == 'JPN')"
# jpn_df = df.query(query)
# min_idx = jpn_df['dollar_price'].idxmax()

# print(min_idx)

for index, row in df.iterrows():
    print(df['date'][index])