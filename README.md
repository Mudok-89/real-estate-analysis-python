# Sreality Zlín Apartments Analysis

Python project focused on web scraping and data analysis of apartment listings from Sreality.cz for the city of Zlín.

## Project background
The goal of this project was to collect current apartment listings from Sreality.cz and prepare the data for further analysis.

## Project workflow

### 1. Web scraping
Using `BeautifulSoup`, the project collects apartment listing data, including:
- apartment URL
- apartment size
- apartment layout
- apartment price
- apartment location

### 2. Data cleaning and ETL
The scraped data is cleaned and transformed to:
- correct data types
- handle missing values
- separate street and city into individual columns
- export cleaned data to CSV

### 3. Data analysis
The cleaned CSV file is loaded into a dataframe and analyzed to answer business and market-related questions about apartment listings in Zlín.

## Analytical questions
- What is the average apartment price in Zlín?
- What is the average apartment price for each apartment layout (for example 1+1, 2+1, 2+kk)?
- What is the average apartment size in square meters for each layout?
- Are there streets with a higher concentration of more expensive apartments?
- Which apartment layout is advertised most frequently in the city, and why might that be the case?
- How can this assumption be supported with data?
- Are there listings with a price above 20,000 CZK? If yes, do these listings also include smaller apartments with a maximum of two rooms (such as 2+1 or 2+kk)?
- What are the minimum and maximum listed prices for each apartment layout?
- Which apartment layout has the largest price range between the minimum and maximum listing price?

## Tools used
- Python
- Jupyter Notebook
- BeautifulSoup
- pandas
- matplotlib
- seaborn

## Skills demonstrated
- web scraping with BeautifulSoup
- HTML parsing
- data extraction from web listings
- data cleaning and preprocessing
- ETL workflow
- handling missing values and data types
- splitting and standardizing location fields
- exporting cleaned data to CSV
- exploratory data analysis in Python
- grouping and aggregation in pandas
- price and apartment layout analysis
- basic data visualization
- deriving insights from external market data

## Business value
This project demonstrates how to collect and prepare external market data for analysis. Similar workflows can be used in market research, pricing analysis, competitive monitoring, or real estate analytics.

## Files in this repository

- `README.md` – project overview, workflow, analytical questions, and key skills demonstrated
- `analysis.py` – cleaned Python script with the core analytical workflow
- `sreality_zlin_analysis.ipynb` – full notebook version containing web scraping, data cleaning, and analysis
- `final_report_EN.pdf` – final report in English
- `data/source_data.csv` – cleaned source dataset used for the analysis
- `docs/project_brief_cz.md` – project brief in Czech
- `docs/project_brief_eng.md` – project brief in English
- `outputs/data_export.xlsx` – exported analytical output
- `outputs/final_report_CZ.pdf` – final report in Czech
- `outputs/final_report_EN.pdf` – final report in English
