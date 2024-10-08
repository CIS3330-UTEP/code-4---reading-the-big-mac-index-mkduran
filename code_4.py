import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')
cc = set(df['iso_a3'].str.lower())

def get_big_mac_price_by_year(year,country_code):
    #cc = set(df['iso_a3'].str.lower()) # removed from code to have for the rest of code 4
    if country_code in cc:
        query = df[(df['iso_a3'].str.lower() == country_code) & (df['date'].str.startswith(str(year)))]
        rounda = round(query['dollar_price'].mean(),2)
    return rounda

def get_big_mac_price_by_country(country_code):
    if country_code in cc:
        query = df[(df['iso_a3'].str.lower() == country_code)]
        roundb = round(query['dollar_price'].mean(),2)
    return roundb


def get_the_cheapest_big_mac_price_by_year(year):
    years = df[df['date'].str.startswith(str(year))]
    cheap_mac = years['dollar_price'].min()
    bob = years.query('dollar_price == @cheap_mac')
    name = bob['name'].iloc[0]
    mac = bob['iso_a3'].iloc[0].upper()
    return f"{name}({mac}): ${cheap_mac:.2f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    years = df[df['date'].str.startswith(str(year))]
    expensive_mac = years['dollar_price'].max()
    bob = years.query('dollar_price == @expensive_mac')
    name = bob['name'].iloc[0]
    mac = bob['iso_a3'].iloc[0].upper()
    return f"{name}({mac}): ${expensive_mac:.2f}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)