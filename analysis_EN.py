# Analysis of apartment listings from `www.sreality.cz`
# 1. Web scraping using `BeautifulSoup` to collect current apartment listings in Zlín
# Goal: collect the following information:
# `apartment URL, apartment size, apartment layout, apartment price, apartment location (street + city)`

from bs4 import BeautifulSoup
import requests

strana = 1
seznam_bytu = []

while True:
    mesto = 'zlin'
    data = requests.get(f'https://www.sreality.cz/hledani/pronajem/byty/{mesto}?strana={strana}').text
    soup = BeautifulSoup(data, 'html.parser')

    """
    ------------------------
    Write your code here
    ------------------------
    """

    # Find all apartment listings
    list_inzeratu = soup.findAll('li', 'MuiGrid-root MuiGrid-item css-l1328q')
    list_inzeratu_filtered = [
        item for item in list_inzeratu
        if not (
            "tip" in item.get("id", "").lower()  # Remove items with "tip" in the ID
            or "adresar" in item.find("a", href=True)["href"]  # Remove agency directory ads
            or "TIP:" in item.get_text()  # Remove items containing "TIP:"
        )
    ]

    for byt in list_inzeratu_filtered:
        odkaz_tag = byt.find('a', href=True)
        odkaz = 'https://www.sreality.cz' + odkaz_tag['href'] if odkaz_tag else None  # apartment URL

        cena_tag = byt.find('p', class_='MuiTypography-root MuiTypography-body1 css-1ndcg2e')  # apartment price
        cena = cena_tag.get_text(strip=True) if cena_tag else "Neuvedeno"

        rozmer_tag = byt.find('p', class_='MuiTypography-root MuiTypography-body1 css-13ztabn')  # apartment size
        if rozmer_tag:
            text = rozmer_tag.get_text(strip=True)
            rozmery = " ".join(text.split()[3:])  # remove the first words from the text
        else:
            rozmery = "Neuvedeno"

        dispozice = byt.find('p', class_='MuiTypography-root MuiTypography-body1 css-13ztabn')  # apartment layout
        if rozmer_tag:
            text = dispozice.get_text(strip=True)
            dispozice = " ".join(text.split()[2:3])  # extract only the layout part
        else:
            dispozice = "Neuvedeno"

        lokace_tag = byt.find_all('p', class_='MuiTypography-root MuiTypography-body1 css-13ztabn')
        lokace = lokace_tag[1].text.strip() if lokace_tag else None

        seznam_bytu.append(
            {
                'url': odkaz,
                'cena': cena,
                'rozmer': rozmery,
                'dispozice': dispozice,
                'lokace': lokace
            }
        )

    """
    ------------------------------------------------------------------------------------------------
    Keep this part below your code - it checks whether the website still contains the "next page"
    button. If not, the program stops.
    ------------------------------------------------------------------------------------------------
    """

    button = soup.find(
        'button',
        'MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedInherit '
        'MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorInherit '
        'MuiButton-root MuiButton-outlined MuiButton-outlinedInherit '
        'MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorInherit css-lp5ywq'
    ).text

    if button != 'Další stránka':
        print('There is no next page. Stopping the scraper.')
        break

    strana += 1
    print(f'Scraping page number {strana}')

    seznam_bytu

# 2. Data analysis - ETL process
# In the first phase, process the data so that it contains correct data types, non-null values, etc.
# Street and city should be stored in separate columns.
# Export the processed and cleaned data to a `.csv` file named `{yourName}_source_data.csv`.
# Start the second part by loading the exported `.csv` file with the scraped data into a dataframe.

# 3. Data analysis
# In the second phase, analyze the data and answer the following questions:
# - What is the average apartment price?
# - What is the average apartment price for each apartment layout (1+1, 2+1, etc.)? Also display it in a chart.
# - What is the average apartment size for each layout?
# - Is there a street with a higher concentration of more expensive apartments?
# - Which apartment layout is advertised most frequently in the city? Which one is it? Why might that be the case?
# - Are there listings priced above 20,000 CZK? If yes, are there also apartments with a maximum of two rooms (2+1 / 2+kk)?
# - Find the minimum and maximum listing price for each apartment layout. Which layout has the largest price range?

import pandas as pd

df = pd.DataFrame(seznam_bytu)
df.to_csv('byty_zlin_kontrola.csv')

# Data outside the while loop so that I can run the code separately
list_inzeratu = soup.findAll('li', 'MuiGrid-root MuiGrid-item css-l1328q')
list_inzeratu_filtered = [
    item for item in list_inzeratu
    if not (
        "tip" in item.get("id", "").lower()  # Remove items with "tip" in the ID
        or "adresar" in item.find("a", href=True)["href"]  # Remove agency directory ads
        or "TIP:" in item.get_text()  # Remove items containing "TIP:"
    )
]

seznam_bytu = []
for byt in list_inzeratu_filtered:
    odkaz_tag = byt.find('a', href=True)
    odkaz = 'https://www.sreality.cz' + odkaz_tag['href'] if odkaz_tag else None  # apartment URL

    cena_tag = byt.find('p', class_='MuiTypography-root MuiTypography-body1 css-1ndcg2e')  # apartment price
    cena = cena_tag.get_text(strip=True) if cena_tag else "Neuvedeno"

    rozmer_tag = byt.find('p', class_='MuiTypography-root MuiTypography-body1 css-13ztabn')  # apartment size
    if rozmer_tag:
        text = rozmer_tag.get_text(strip=True)
        rozmery = " ".join(text.split()[3:])  # remove the first words from the text
    else:
        rozmery = "Neuvedeno"

    dispozice = byt.find('p', class_='MuiTypography-root MuiTypography-body1 css-13ztabn')  # apartment layout
    if rozmer_tag:
        text = dispozice.get_text(strip=True)
        dispozice = " ".join(text.split()[2:3])  # extract only the layout part
    else:
        dispozice = "Neuvedeno"

    lokace_tag = byt.find_all('p', class_='MuiTypography-root MuiTypography-body1 css-13ztabn')
    lokace = lokace_tag[1].text.strip() if lokace_tag else None

    seznam_bytu.append(
        {
            'url': odkaz,
            'cena': cena,
            'rozmer': rozmery,
            'dispozice': dispozice,
            'lokace': lokace
        }
    )
    print(seznam_bytu)

# DATA PROCESSING
import pandas as pd

df = pd.read_csv('byty_zlin.csv')  # name on GitHub is 'source_data.csv'

df.head()
df.info()

# CLEANING AND TYPE CONVERSION

# I want to convert price to numeric, so I need to clean it first
# Remove currency, extra spaces, and the text "měsíc"
df['cena'] = df['cena'].str.replace('Kč/měsíc', '').str.replace(' ', '').str.replace(r'\xa0', ' ', regex=True).str.replace(r'\s+', '', regex=True)
df['cena'] = pd.to_numeric(df['cena'], errors='coerce')
df['cena']  # price changed to float64

df.info()  # price changed to float64

df['cena'] = df['cena'].fillna(0)  # missing values will be replaced with 0
df['cena'] = df['cena'].astype(int)  # convert price from float to integer
df['cena']

# CLEANING AND ADJUSTING THE LOCATION VARIABLE
print(df['lokace'].unique())  # check unique values in the location column

df['ulice'] = df['lokace'].str.split(',').str[0]  # keep only the part before the comma (street)
df['ulice']

print(df['rozmer'].unique())  # check unique values in the size column

# DATA ANALYSIS
# 1. AVERAGE APARTMENT PRICE

prumerna_cena_bytu = df['cena'].mean()
print(f'The average apartment price is {prumerna_cena_bytu} CZK.')

# 2. Average apartment price for each layout and chart display
df['dispozice'] = df['dispozice'].str.strip()  # remove leading and trailing spaces
print(df['dispozice'].unique())  # check unique layout values

df_prumerne_ceny = df.groupby('dispozice')['cena'].mean().reset_index()
df_prumerne_ceny = df_prumerne_ceny.assign(cena=df_prumerne_ceny['cena'].round(2)).sort_values(by='cena', ascending=False)
df_prumerne_ceny

df_prumerne_ceny.to_excel("č.2_prumerne_ceny_dispozice.xlsx", index=False, engine='openpyxl')

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(df_prumerne_ceny['dispozice'], df_prumerne_ceny['cena'], color='orange')

plt.xlabel('Apartment Layout')
plt.ylabel('Average Price (CZK)')
plt.title('Average Apartment Price by Layout')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

!pip install xlsxwriter

# Create an Excel file with a chart
with pd.ExcelWriter("č.2graf_ceny.xlsx", engine="xlsxwriter") as writer:
    df_prumerne_ceny.to_excel(writer, sheet_name="Data", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Data"]

    chart = workbook.add_chart({"type": "column"})
    chart.add_series({
        "categories": ["Data", 1, 0, len(df_prumerne_ceny), 0],
        "values": ["Data", 1, 1, len(df_prumerne_ceny), 1],
        "name": "Average Apartment Price"
    })

    worksheet.insert_chart("E2", chart)

# 3. What is the average apartment size for each layout?

df['rozmer'] = df['rozmer'].str.replace('m²', '', regex=True).str.strip()
df['rozmer'] = pd.to_numeric(df['rozmer'], errors='coerce')

df_prumerne_rozmery = df.groupby('dispozice')['rozmer'].mean().reset_index().round(2)
df_prumerne_rozmery.columns = ['dispozice', 'prumerne_rozmery']
df_prumerne_rozmery

df_prumerne_rozmery.to_excel("č.3_prumerne_rozmery.xlsx", index=False, engine='openpyxl')

# 4. Is there a street with a higher concentration of more expensive apartments?

df_prumerna_cena_ulice = df.groupby('ulice')['cena'].mean().reset_index().round(2)
df_prumerna_cena_ulice.columns = ['ulice', 'prumerna cena']
df_prumerna_cena_ulice.head(10)

df_prumerna_cena_ulice.to_excel("č.4_prumerna_cena_ulic.xlsx", index=False, engine='openpyxl')

# Sort streets from the most expensive to the least expensive
df_prumerna_cena_ulice = df_prumerna_cena_ulice.sort_values(by='prumerna cena', ascending=False)
top_10_ulic = df_prumerna_cena_ulice.head(10)
top_10_ulic

top_10_ulic.to_excel("č.4b_top_10_ulic.xlsx", index=False, engine='openpyxl')

# Visualize the top streets with the highest average apartment price
plt.figure(figsize=(12, 6))
plt.barh(top_10_ulic['ulice'], top_10_ulic['prumerna cena'], color='skyblue')
plt.xlabel('Average Price (CZK)')
plt.ylabel('Street')
plt.title('Top 10 Streets with the Highest Average Apartment Prices')
plt.gca().invert_yaxis()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Save the chart as an image
plt.figure(figsize=(12, 6))
plt.barh(top_10_ulic['ulice'], top_10_ulic['prumerna cena'], color='skyblue')
plt.xlabel('Average Price (CZK)')
plt.ylabel('Street')
plt.title('Top 10 Streets with the Highest Average Apartment Prices')
plt.gca().invert_yaxis()
plt.savefig("graf_ulice.png", dpi=300, bbox_inches="tight")
plt.close()

# Create an Excel file and insert the image
with pd.ExcelWriter("top_ulice.xlsx", engine="xlsxwriter") as writer:
    top_10_ulic.to_excel(writer, sheet_name="Data", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Data"]

    worksheet.insert_image("D2", "graf_ulice.png")

# 5. Which apartment layout is advertised most frequently?

df_dispozice_counts = df['dispozice'].value_counts().reset_index()
df_dispozice_counts

# Rename columns for clarity
df_dispozice_counts.columns = ['dispozice', 'pocet_inzeratu']
df_dispozice_counts
df_dispozice_counts.to_excel("Pocet_vyskytu_kompozice.xlsx", index=False, engine='openpyxl')

# 6. Are there listings priced above 20,000 CZK?
# If yes, are there also apartments with a maximum of two rooms (2+1 / 2+kk)?

df_drahe_byty = df[df['cena'] > 20000]
df_drahe_male_byty = df_drahe_byty[df_drahe_byty['dispozice'].isin(['2+1', '2+kk'])]
df_drahe_male_byty

df_drahe_male_byty.to_excel("inzerce_drahych_malych_bytu.xlsx", index=False, engine='openpyxl')

# 7. Find minimum and maximum listing prices for each apartment layout.
# Which layout has the largest price range?

df_ceny_rozptyl = df.groupby('dispozice')['cena'].agg(['min', 'max'])
df_ceny_rozptyl['rozptyl'] = df_ceny_rozptyl['max'] - df_ceny_rozptyl['min']
df_ceny_rozptyl

df_ceny_rozptyl.to_excel("č.7_ceny_rozptyl_kompozice.xlsx", index=False, engine='openpyxl')

# Find the layout with the largest price range
nejvetsi_rozptyl_dispozice = df_ceny_rozptyl['rozptyl'].idxmax()
nejvetsi_rozptyl_hodnota = df_ceny_rozptyl['rozptyl'].max()

print(f"The largest price range is for layout {nejvetsi_rozptyl_dispozice} with a range of {nejvetsi_rozptyl_hodnota} CZK.")

# Grouped data for possible Excel export
df_grouped_ceny = df.groupby('dispozice')['cena'].agg(['min', 'max', 'mean']).reset_index()
df_grouped_ceny

df_grouped_ceny.to_excel("č.prumerne_ceny_dispozice.xlsx", index=False, engine='openpyxl')

df_grouped_velikost = df.groupby('dispozice')['rozmer'].mean().reset_index()
df_grouped_velikost

df_pocty_dispozic = df['dispozice'].value_counts().reset_index()
df_pocty_dispozic.columns = ['dispozice', 'pocet']
df_pocty_dispozic

df_pocty_dispozic.to_excel("č.pocty_dispozic.xlsx", index=False, engine='openpyxl')

pip install pandas openpyxl

df.to_excel("datova_analytika_bytu.xlsx", index=False, engine='openpyxl')
