import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd



def fetch_from_trustpilot(company_website, 
                          company_name, 
                          first_page_num, 
                          final_page_num):
    """
    Function web scrapes reviews of a specific company from trustpilot
    Parameters: 
        - company_website :  type str, the url of website
        - company_name :   type str, the company we are investigating
        - first_page_num : type int, first page of reviews we are looking at
        - final_page_num : type int, final page of reviews we are looking at

    Returns:
        - review_titles -> type list
        - review_text -> type list
        - stars_number -> type list
        - date_list -> type list
        - compnay_list -> type list
    """
    # Where data will be saved to in preparation for making the dataframe
    date_list = []
    review_titles = []
    review_text = []
    stars_number = []
    company_names = []

    for i in range(first_page_num,final_page_num):
        response = requests.get(f'https://www.trustpilot.com/review/{company_website}?page={i}')
        try:
            if response.status_code == 200:
                webpage = response.text
                soup = BeautifulSoup(webpage, 'html.parser')

                # All reviews are in a div with that class name
                all_reviews = soup.find_all('div', {'class':'styles_reviewCardInner__EwDq2'})
                
                for review in all_reviews:
                    # h2 is a tag that holds the title
                    title_tag = review.find('h2')
                    # p is the tag that holds the review description
                    text_tag = review.find('p')
                    # time is the tag that holds the time
                    time_tag = review.find('time')
                    # where the stars are are in the img tag
                    stars_tag = review.find('img')

                    review_titles.append(title_tag.text)
                    review_text.append(text_tag.text)
                    stars_number.append(stars_tag.get('alt'))
                    date_list.append(time_tag.text)
                    company_names.append(company_name)
        except ConnectionError:
            print("Error fetching data")
    return review_titles, review_text, stars_number, date_list, company_names


def create_data_frame(company_names,titles,reviews,ratings,dates):
    """
    A function that creates data frame from given data lists
    Parameters:
        - company_names -> a list of company_names, all values are the same
        - titles -> a list of titles of reviews scraped
        - reviews -> a list of reviews scraped
        - ratings -> a list of ratings for every review
        - dates -> a list of dates 
    Return Variables:
        - A data frame that has all of the data above combined in a table
    """
    dict = {'Company Name':company_names, 'Title of Review': titles, 'Review Description': reviews, 
            'Date of Review': dates, 'No. of stars': ratings}
    return pd.DataFrame.from_dict(dict)

