import pandas as pd

df = pd.read_csv('./big-mac-full-index.csv')
df['date'] = pd.to_datetime(df['date'])
df['year']=df['date'].dt.year
df_year_iso = df[['year','iso_a3']]
print(df_year_iso)





#print(df)

# country_code = "JPN" # i dont need to do this on Code 4

# query_text = f"(iso_a3 == '{country_code}')"

# print(len(df))
# sub_df = df.query(query_text)
# print(len(sub_df))

# print(sub_df)

# # print(sub_df.loc[21])
# # ("/n")
# # print(sub_df.iloc[21])

# print(sub_df['dollar_price'].mean())


# new_query = f"date > '2012-01-01' and date < '2012-12-31'"

# new_date_df = df.query(new_query)

# print(new_date_df)
