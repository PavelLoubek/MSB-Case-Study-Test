# MSB-Case-Study-Test

## Jak řešení spustit/zapnout na jiném počítači:

### S nainstalovaným Pythonem (spuštěno ve virtuálním prostředím)

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

### Pomocí exportovaného exe souboru (nepraktické, ale udělané pro jednoduchost)

Stačí mít někde uložený .exe soubor a u ní složku input, ve které se nachází .csv soubory. Output složka se vytvoří sama. Dal jsem to pouze jako příklad rychlého řešení.

## Jak přidat nové vstupní soubory

Stačí přidat do složky input. Vezme si to veškeré .csv soubory. 

(Dalo by se předělat samozřejmě na jiné formáty, každopádně pro tento příklad jsem si vybral .csv, klasický reportovací formát)

## Jak řešení udržovat

Při změně struktury lze změnit v kódu. Zde v příkladu pod proměnnou *requiredColumns*



# Rychlé zbytky odpovědí pro diskuzi:

**Jaké technologie nebo nástroje byste použili?**

Já si vybral Python, mám v něm nějakou znalost a podobné řešení jsem si již zkoušel. Určitě by šla potencionální automatizace přes nějaký Make.com, Zapier a jiný, který by dokázal šahat třeba do Sharepointu, každopádně tohle si dokážu vytvořit v domácím prostředí, dá se to pustit lokálně a zvládnu to vytvořit rychle.

**Uveďte možné problémy (např. nekonzistentní data) a jak je řešit.**

Neudělal jsem tolik kontrol, aby program byl bezproblémový (to ani nikdy na 100% nebude). Každopádně pár základních kontrol jsem udělal, zbytek by se s více časem odladil, i dle tabulky a používání.

Každopádně očekával bych využití finálního vygenerovaného reportu v nějakém PowerBI, kde by si ho někdo dál zpracoval.