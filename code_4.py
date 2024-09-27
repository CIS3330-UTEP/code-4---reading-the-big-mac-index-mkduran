import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')
# df['year']= df['date'].str[:4]
# df['iso_a3']=df['iso_a3'].str.lower()
# df['dollar_price'] = df['dollar_price'].mean()
# year_country_price=df[['year','iso_a3','dollar_price']]
# print(round(year_country_price,2))


def get_big_mac_price_by_year(year,country_code):
    #df = pd.read_csv('./big-mac-full-index.csv')
    df['year']= df['date'].str[:4]
    df['iso_a3']=df['iso_a3'].str.lower()
    df['dollar_price'] = df['dollar_price'].mean()
    year_country_price=df[['year','iso_a3','dollar_price']]
    print(round(year_country_price),2)

def get_big_mac_price_by_country(country_code):
    pass
    # df['iso_a3']=df['iso_a3'].str.lower()
    # df['dollar_price'] = df['dollar_price'].mean()
    # country_price=df[['iso_a3','dollar_price']]
    # return(country_price)

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,'arg')
    print(result_a)