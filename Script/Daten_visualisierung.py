import matplotlib.pyplot as plt
import seaborn as sns

# Verteilung des Alters der Kunden
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=True)
plt.title('Verteilung des Alters der Kunden')
plt.xlabel('Alter')
plt.ylabel('Häufigkeit')
plt.show()
