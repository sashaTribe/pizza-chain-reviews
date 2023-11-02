from fetch_data import fetch_from_trustpilot, create_data_frame
import pandas as pd
import csv

CHAIN_LIST = ['www.prezzorestaurants.co.uk','www.zizzi.co.uk','francomanca.co.uk','www.pizzaexpress.com']
FILE_NAMES = ['prezzo_df.csv', 'zizzi_df.csv', 'fm_df.csv', 'pizza_express_df.csv']
COMPANY_LIST = ['Prezzo', 'Zizzi', 'Franco Manca', ' Pizza Express']

def make_df_files():
    START_PAGE = 1
    END_PAGE  = 12
    df_list = []

    for i in range(len(CHAIN_LIST)):
        temp_titles, temp_reviews, temp_ratings, temp_dates, company_names  = fetch_from_trustpilot(CHAIN_LIST[i],
                                                                                     COMPANY_LIST[i],
                                                                                    START_PAGE,
                                                                                    END_PAGE)
        temp_df = create_data_frame(company_names,
                                    temp_titles, temp_reviews,
                                    temp_ratings, temp_dates)
        df_list.append(temp_df)
    i = 0
    for df in df_list:
        df.to_csv(FILE_NAMES[i], sep=',', index=True, encoding='utf-8')
        i += 1

make_df_files()