# Analýza bytů ve Zlíně

Projekt se dělí na tři části.

## 1. Web Scraping
Zdroj: `www.sreality.cz`

Pomocí knihovny `BeautifulSoup` získejte všechny aktuální inzerce bytů ve vybraném městě.

Získejte následující informace:
- URL odkaz bytu
- rozměry bytu
- kompozice bytu
- cena bytu
- lokace bytu (ulice + město)

## 2. Datová analýza – ETL proces
V první fázi proveďte zpracování dat tak, aby obsahovala správné datové typy, nenulové hodnoty a další potřebné úpravy.

Ulice a město budou uloženy v samostatných sloupcích.

Zpracovaná a vyčištěná data vyexportujte do `.csv` souboru s názvem `{vašeJméno}_zdrojová_data.csv`.

Druhou část začněte tím, že do dataframe načtete vámi vyexportovaný `.csv` soubor s vyscrapovanými daty.

## 3. Datová analýza
Ve druhé fázi proveďte analýzu dat a odpovězte na následující otázky:

- Jaká je průměrná cena bytů?
- Jaká je průměrná cena bytů pro každou kompozici, například 1+1, 2+1 atd.? Výsledek zobrazte také v grafu.
- Jaká je průměrná velikost bytu v m² pro každou dispozici?
- Existuje ulice, kde je vyšší koncentrace dražších bytů?
- Jaký typ kompozice je v daném městě nejčastěji inzerován? Který to je? Proč si myslíte, že tomu tak je? Jak to můžeme potvrdit daty?
- Existují zde inzerce bytů, které stojí více než 20 000 Kč? Pokud ano, jsou v této cenové hladině inzerovány i maximálně dvoupokojové byty (2+1 / 2+kk)?
- Zjistěte minimální a maximální inzerovanou cenu pro každou kompozici bytu. Která kompozice má největší rozdíl mezi minimální a maximální inzerovanou cenou?
