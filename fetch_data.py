import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

start_page = 1
end_page = 19

date_list = []
review_titles = []
review_text = []
stars_number = []
#__next > div > div > main > div > div.styles_mainContent__nFxAv > section > div:nth-child(4) > article > div
#__next > div > div > main > div > div.styles_mainContent__nFxAv > section > div:nth-child(8) > article > div > section > div.styles_reviewContent__0Q2Tg > p.
for i in range(start_page,end_page):
    response = requests.get(f'https://www.trustpilot.com/review/www.prezzorestaurants.co.uk?page={i}')
    try:
        if response.status_code == 200:
            webpage = response.text
            soup = BeautifulSoup(webpage, 'html.parser')
            all_reviews = soup.find_all('div', {'class':'styles_reviewCardInner__EwDq2'})
            
            for review in all_reviews:
                title_tag = review.find('h2')
                text_tag = review.find('p')
                time_tag = review.find('time')
                stars_tag = review.find('img')

                review_titles.append(title_tag.text)
                review_text.append(text_tag)
                stars_number.append(stars_tag.get('alt'))
                date_list.append(time_tag)


                """
                text_tags = review.get('p', {'class':'typography_body-l__KUYFJ.typography_appearance-default__AAY17.typography_color-black__5LYEn'})
                text = text_tags.text

                time_tags = soup.find_all('time')
                review_title = tag.text
                """
                
                #review_titles.append(title)
            
           
    except ConnectionError:
        print("Error fetching data")
"""
print("Length of list: ", len(review_titles))
for title in review_titles:
    print(title)
print(len(review_titles))
print(len(review_text))
print(len(date_list))
print(len(stars_number))
"""

dictionary = {'Title of Review': review_titles, 'Review Description': review_text, 'Date of Review': date_list, 'No. of stars': stars_number}
test_df = pd.DataFrame.from_dict(dictionary)

print(test_df.head(10))

def fetch_from_trustpilot(company_name, first_page_num, final_page_num):
    date_list = []
    review_titles = []
    review_text = []
    stars_number = []

    for i in range(first_page_num,final_page_num):
        response = requests.get(f'https://www.trustpilot.com/review/{company_name}?page={i}')
        try:
            if response.status_code == 200:
                webpage = response.text
                soup = BeautifulSoup(webpage, 'html.parser')
                all_reviews = soup.find_all('div', {'class':'styles_reviewCardInner__EwDq2'})
                
                for review in all_reviews:
                    title_tag = review.find('h2')
                    text_tag = review.find('p')
                    time_tag = review.find('time')
                    stars_tag = review.find('img')

                    review_titles.append(title_tag.text)
                    review_text.append(text_tag.text)
                    stars_number.append(stars_tag.get('alt'))
                    date_list.append(time_tag.text)
        except ConnectionError:
            print("Error fetching data")
    return review_titles, review_text, stars_number, date_list

def create_data_frame(titles,reviews,ratings,dates):
    dict = {'Title of Review': titles, 'Review Description': reviews, 
            'Date of Review': dates, 'No. of stars': ratings}
    return pd.DataFrame.from_dict(dict)

