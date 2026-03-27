# Apartment Analysis in Zlín

The project is divided into 3 parts:

## 1. Web Scraping
- Source: `www.sreality.cz`
- Using the `BeautifulSoup` library, collect all current apartment listings in the selected city.
- Extract the following information:
  - apartment URL
  - apartment size
  - apartment layout
  - apartment price
  - apartment location (street + city)

## 2. Data Analysis – ETL Process
- In the first phase, process the data so that it contains the correct data types, non-null values, and other necessary cleaning steps.
- Street and city should be stored in separate columns.
- Export the processed and cleaned data into a `.csv` file named `{yourName}_source_data.csv`.
- Start the second part by loading the exported `.csv` file with the scraped data into a dataframe.

## 3. Data Analysis
In the second phase, analyze the data and answer the following questions:

- What is the average apartment price?
- What is the average apartment price for each apartment layout (for example 1+1, 2+1, etc.)? Also display the result in a chart.
- What is the average apartment size in square meters for each apartment layout?
- Is there a street with a higher concentration of more expensive apartments?
- Which apartment layout is advertised most frequently in the city? Which one is it? Why do you think this is the case? How can we confirm it with data?
- Are there listings with a price higher than 20,000 CZK? If yes, are there also listings in this price range for apartments with a maximum of two rooms (2+1 / 2+kk)?
- Find the minimum and maximum listing price for each apartment layout. Which layout has the largest spread between the minimum and maximum listed price?
