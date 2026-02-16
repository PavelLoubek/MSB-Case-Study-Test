# Modules - pandas pro merge csv souborů, glob pro získání seznamu všech csv souborů v adresáři, os pro práci s cestami k souborům, datetime pro získání aktuálního data a času pro pojmenování výstupního souboru
import pandas as pd
import glob
import os
import datetime

date = datetime.datetime.now().strftime("%d%m%Y")
inputFolder = "./input"
outputFolder = "./output"
outputFile = date + "_merged_report.csv"

requiredColumns = ["Date", "Client", "Product", "Quantity", "Revenue"]

def LoadFiles():
    allFiles = glob.glob(os.path.join(inputFolder, "*.csv"))
    allData = []
    for file in allFiles:
        data = pd.read_csv(file)
        if all(col in data.columns for col in requiredColumns):
            allData.append(data)
            print(f"Soubor '{file}' byl úspěšně načten.")
        else:
            raise ValueError(f"Soubor '{file}' neobsahuje všechny požadované sloupce. Přeskakuji tento soubor.")
    return pd.concat(allData, ignore_index=True)

def CleanData(data):
    data = data.drop_duplicates()
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data["Quantity"] = pd.to_numeric(data["Quantity"], errors='coerce')
    data["Revenue"] = pd.to_numeric(data["Revenue"], errors='coerce')
    return data.dropna(subset=["Date", "Client", "Product", "Quantity", "Revenue"])

def SortData(data):
    return data.sort_values(by=["Date", "Client", "Product"])

def Main():
    try:
        data = LoadFiles()
        data = CleanData(data)
        data = SortData(data)
        os.makedirs(outputFolder, exist_ok=True)
        outputPath = os.path.join(outputFolder, outputFile)
        data.to_csv(outputPath, index=False)
        print(f"Sloučený report byl úspěšně uložen do '{outputPath}'")
    except Exception as e:
        print(f"Došlo k chybě: {e}")

if __name__ == "__main__":
    Main()
    input("Zmáčkni Enter pro ukončení...")