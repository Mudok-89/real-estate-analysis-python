# Sreality Zlín Apartments Analysis

Python project focused on web scraping and data analysis of apartment listings from Sreality.cz for the city of Zlín.

## Project background
The goal of this project was to collect current apartment listings from Sreality.cz and prepare the data for further analysis.

## Project tasks
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
The cleaned CSV file is loaded back into a dataframe and used for further analysis of apartment listings in Zlín.

## Tools used
- Python
- Jupyter Notebook
- BeautifulSoup
- pandas

## Files in this repository
- `sreality_zlin_analysis.ipynb` – full notebook with scraping, cleaning, and analysis
- `analysis.py` – cleaned Python script version of the core workflow
- `yourname_zdrojova_data.csv` – cleaned dataset
- `project_brief_cz.md` or `project_brief.pdf` – project assignment in Czech

## Skills demonstrated
- web scraping
- HTML parsing
- data cleaning
- ETL workflow
- working with missing values
- CSV export
- dataframe analysis
- Python data analysis

## Business value
This project demonstrates how to collect and prepare external market data for analysis. Similar workflows can be used in market research, pricing analysis, competitive monitoring, or real estate analytics.
