from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Beispielmerkmale und Zielvariable
X = df[['age', 'annual_income', 'purchase_count']]  # Merkmale
y = df['total_spent']  # Zielvariable

# Aufteilen der Daten in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Erstelle und trainiere das Modell
model = LinearRegression()
model.fit(X_train, y_train)

# Vorhersagen und Bewertung des Modells
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f'Mean Squared Error: {mse}')
