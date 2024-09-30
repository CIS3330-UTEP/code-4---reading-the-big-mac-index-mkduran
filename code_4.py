import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')
cc = df['iso_a3'].str.lower()
#print(cc)
years = df['date'].str[:4]
#print(years)

def get_big_mac_price_by_year(year,country_code):
    if country_code in cc:
        query = df(df['iso_a3'] == cc) & (df['date'] == years)
        round1 = round(query['dollar_price'].mean(),2)
        return round1

def get_big_mac_price_by_country(country_code):
    pass

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass