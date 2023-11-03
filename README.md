# Pizza-Chain-Reviews
#### Author: Alexandra (Sasha) Tribe

## Table of Contents :)
- [Description](#description)
- [Technologies Used](#technologies-used)
- [The workflow](#the-workflow)
    - [Python](#python)
    - [Power BI](#power-bi)
- [What I struggled with](#what-I-struggled-with)
- [The Future State](#the-future-state)
- [Acknowledgements](#acknowledgments)


## Description
Analysing customer reviews for sentimental analysis between different pizza chains. The audience are the owners of those food chains so they can see what is going well and what is not going well and what their competitors are like.

## Technologies used:
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
- ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
- ![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
- ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
- NLTK
- Requests
- BeautifulSoup
- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

What is already provided for you:
- All the data frames are in [df_files](/df_files/)
- If you want to run all of them, on the terminal run: 

    python /build_dataset/create_datasets.py

Then you can go straight to [the notebook](pizza-chain-reviews/notebook_pizza)

## The workflow

### Python

1. Web scrape data from f'https://www.trustpilot.com/review/www.prezzorestaurants.co.uk?page={i}'
    - i representing the page
    - We are interseted in : 
        - Title
        - Review
        - Date issued
        - Its' ratings

    - This data is scraped using the module Beautiful Soup

2. Putting all the data onto a data frame
3. I did put it all onto an SQL database but with the time I had, eventually there was no use 
4. I chose to look at the Prezzo dataframe, and so I loaded the data from the csv file onto a data frame for:
    - Data Inspection: checked its datatypes, it's word count distribution, null values, unnecessary columns
    - Data Cleaning: I used NLTK to tokenize, lemmatize the reviews as well as importing their stopword datasets to remove words that have little meaning/value to the head of the company. This is also to encourage faster processing of data.
    - I noticed there were emojis written in the comments so I added a function from slowkow/remove-emoji.py to achieve this
5. Have created a new column that classifies a review either in positive, neutral, or negative based on rating where:
     - 1-2 stars means its negative
     - 3 stars is neutral
     - 4-5 stars is positive

6. Added every word from the review to a specific list that matches with its' sentiment value
7. Created several frequency distributions from NLTK and visualised its result before moving on to Power BI. 
    - I have gone back a few cells of code as I recognised words that did not have much value on its own e.g., numbers with no context
8. I converted every frequency distribution to a dataframe and saved it onto a csv file to load onto power bi

### Power BI 

- The graphs I wanted to build for the client:
    - A word cloud: so they can get a gist of common words on a certain type of review
    - A frequency bar plot: so they know how often that particular word pops up and understand if that is a pending issue
    - A line graph: A line graph showing the frequency of the different types of ratings over time
        - This will help them have a good understanding of how they are doing now as a restaurant chain

1. Load the data from csv file then transform the data onto my query editor
    - Imported 4 different csv files:
        - prezzo_data.csv
        - pos_freq_df
        - neu_freq_df
        - neg_freq_df
    - Removed any nulls
    - Changed 'Date of Review' to Date type
    - Broke the table down into 'Date of Review', 'Sentiment Level' and 'Ratings' and called this table *Date vs Sentiment*
    - 

2. Built a line chart showing the trends of the different types of ratings over two years

3. For the rest of the tables I created a word cloud and a word distribution bar plot

4. Created a page showing the same graphs but for different semantic types: 

![Power Bi Example](/Images/power_bi_ex.png)


## What I struggled with:
- I struggled with coming up with ways to showcase sentimental analysis
- I struggled to load everything to SQL and use SQL
    -  I wanted to use SQL because it takes longer to fetch some data from a Pandas dataframe than SQL, hence I wanted to use SQL to clean and load my data properly
- NLTK was tricky, might have overcomplicated the problem trying to use NLTK's sentimental analysis instead of sticking to the what the ratings shows from the beginning


## The Future State
- Applying these methods to all the data frames/ companies
    - Then create a graph to compare each company as competitors
- Create an airflow to manage the pipeline better and help make the flow of data more automated
- For the long future:
    - **Would be fantastic to build a web scraper pipeline where it fetches the most recent review and guesses its semantic tone without taking in the ratings to save resources**

## Acknowledgement
- Thank you to Xander Talent peer for the moral support