import pandas as pd

df = pd.read_csv('./big-mac-full-index.csv')
print(df)

# country_code = "JPN" # i dont need to do this on Code 4
# df['iso_a3'] = df['iso_a3'].str.lower()
# query_text = df['iso_a3']
# print(query_text)

# # print(len(df))
# sub_df = df.query(query_text)
# print(len(sub_df))

# print(sub_df)

# print(sub_df.loc[21])
# ("/n")
# print(sub_df.iloc[21])

# print(sub_df['dollar_price'].mean())


new_query = f"date > '109-01-01' and date < '2024-12-31'"

new_date_df = df.query(new_query)

print(new_date_df)
