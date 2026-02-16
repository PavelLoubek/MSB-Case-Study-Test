# Modules - pandas pro merge csv souborů, glob pro získání seznamu všech csv souborů v adresáři, os pro práci s cestami k souborům, datetime pro získání aktuálního data a času pro pojmenování výstupního souboru
import pandas as pd
import glob
import os
import datetime

date = datetime.datetime.now().strftime("%d%m%Y")
inputFolder = "../input"
outputFolder = "../output"
outputFile = date + "_merged_report.csv"