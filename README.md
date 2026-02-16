# MSB-Case-Study-Test

**Jak řešení spustit/zapnout na jiném počítači:**
1. S nainstalovaným Pythonem (spuštěno ve virtuálním prostředím)
Otevřít powershell
Dostat se do složky s projektem - např.: cd .\MSB-Case-Study-Test
Založení virtuálního prostředí (jednoduchost kompatibility díky udržování verzí modulů) - python -m venv venv
Aktivate virtuálního prostředí - venv\scripts\activate
Instalace modulů - pip install -r requirements.txt
Spustit projekt - python src/main.py
```
cd .\MSB-Case-Study-Test
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
python src/main.py
```
2. Pomocí exportovaného exe souboru (nepraktické, ale udělané pro jednoduchost)
Je třeba mít ten projekt i tak stažený (převážně kvůli složkám), každopádně šlo by programově upravit. Dal jsem to pouze jako rychlé řešení.

**Jak přidat nové vstupní soubory**
Stačí přidat do složky input. Vezme si to veškeré .csv soubory. (Dalo by se předělat samozřejmě na jiné formáty, každopádně pro tento příklad jsem si vybral .csv, klasický reportovací formát)

**Jak řešení udržovat**
Při změně struktury lze změnit v kódu. Zde v příkladu pod proměnnou *requiredColumns*