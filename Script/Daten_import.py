import pandas as pd

# Lade die CSV-Datei in einen DataFrame
df = pd.read_csv('E:\Ausbildung\Projekte\Data-Science-Coding-Challenge\src\ecommerce_customer_data.csv')  # Passe den Pfad zur Datei an

# Zeige die ersten fünf Zeilen des DataFrames an
print(df.head())

# Gebe die grundlegenden Informationen über den DataFrame aus
print(df.info())

# Überprüfe, ob es fehlende Werte gibt
print(df.isnull().sum())

# Statistische Zusammenfassungen
print(df.describe())

