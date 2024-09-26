import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    df['date'] = pd.to_datetime(df['date'])
    df['year']=df['date'].dt.year
    df['iso_a3']=df['iso_a3'].str.lower()
    df_year_iso = df[['year','iso_a3']]
    print(df_year_iso)

def get_big_mac_price_by_country(country_code):
     pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,'arg')
    print(result_a)