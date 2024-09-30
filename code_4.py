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
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
