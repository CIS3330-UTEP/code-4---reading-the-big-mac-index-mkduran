import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    df['year'] = df['date'].str[:4]
    df['iso_a3'] = df['iso_a3'].str.lower()
    year_country = df[(df['year'] == year) & (df['iso_a3'] == country_code)]
    mean_price = year_country['dollar_price'].mean()
    return(round(mean_price,2))
    # df['year']= df['date'].str[:4]
    # df['iso_a3']=df['iso_a3'].str.lower()
    # price = df['dollar_price'].mean().round(2)
    # year_country_price=df[['year','iso_a3']].copy()
    # year_country_price['price'] = price
    # print(year_country_price)

def get_big_mac_price_by_country(country_code):
    pass

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass