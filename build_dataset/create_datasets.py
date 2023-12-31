from fetch_data import fetch_from_trustpilot, create_data_frame
import pandas as pd
import csv

# list of websites of representing different pizza chains
CHAIN_LIST = ['www.prezzorestaurants.co.uk','www.zizzi.co.uk','francomanca.co.uk','www.pizzaexpress.com']

# list of file names I want certain data to be saved to
FILE_NAMES = [
    'df_files/original_pizza_chain_dfs/prezzo_df.csv', 
    'df_files/original_pizza_chain_dfs/zizzi_df.csv',
    'df_files/original_pizza_chain_dfs/fm_df.csv',
    'df_files/original_pizza_chain_dfs/pizza_express_df.csv'
                 ]

# Companies I am analysing (or want to analyse)
COMPANY_LIST = ['Prezzo', 'Zizzi', 'Franco Manca', ' Pizza Express']
 
# creates a data frame for every pizza chain the lists above then saves to
# a file.
def make_df_files():
    # only taking 12 pages worth of reviews into account
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