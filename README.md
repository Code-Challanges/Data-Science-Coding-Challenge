# Data-Science-Coding-Challenge
Data Science Coding-Challenge, die sowohl deine Fähigkeiten in der Datenaufbereitung, Analyse und Modellierung testet. Diese Challenge könnte in einem Bewerbungsprozess für eine Data-Science-Rolle verwendet werden

# Problemstellung

Kundensegmentierung und Umsatzprognose

Du arbeitest für ein E-Commerce-Unternehmen, das eine große Menge an Kundendaten gesammelt hat. Das Unternehmen möchte seine Kunden besser verstehen und personalisierte Marketingmaßnahmen ergreifen, um den Umsatz zu steigern.

Deine Aufgabe ist es, basierend auf den vorhandenen Daten:
 1. Die Kunden in sinnvolle Segmente zu unterteilen
 2. Ein Modell zu entwickeln, das den Umsatz der Kunden für die nächsten 30 Tage vorhersagt

# Datenbeschreibung
Du erhältst einen Datensatz mit den folgenden Spalten:

| Spalte                     | Beschreibung                                                                                     |
|----------------------------|--------------------------------------------------------------------------------------------------|
| customer_id                | Eindeutige ID des Kunden                                                                         |
| age	                     | Alter des Kunden                                                                                 |
| gender                     | Geschlecht des Kunden (männlich, weiblich, divers)                                               |
| annual_income              | Jährliches Einkommen des Kunden in USD                                                           |
| purchase_amount            | Betrag des letzten Kaufs in USD                                                                  |	                
| purchase_count             | Anzahl der Käufe des Kunden in den letzten 12 Monaten                                            |                 
| join_date	                 | Datum, an dem der Kunde dem Unternehmen beigetreten ist                                          |                 
| last_purchase_date         | Datum des letzten Kaufs	                                                                        |
| avg_purchase_interval_days | Durchschnittlicher Zeitraum zwischen Käufen (in Tagen)                                           |            
| total_spent                | Gesamtbetrag, den der Kunde bisher ausgegeben hat                                                |
| next_purchase_prediction	 | (Optional) Vorhersage, wann der nächste Kauf erfolgt (in Tagen)                                  |
| label_churn	             | 1, wenn der Kunde wahrscheinlich abwandert, 0, wenn nicht (nur für den zweiten Teil der Aufgabe) |





# Aufgaben


# Teil 1: Kundensegmentierung

Datenaufbereitung
- Bereinige den Datensatz, entferne fehlende Werte und überprüfe die Daten auf Inkonsistenzen.
- Erstelle sinnvolle Merkmale (Features), die zur Segmentierung der Kunden beitragen können.

Clustering-Modell
- Wähle einen geeigneten Algorithmus (z. B. K-Means, DBSCAN, Hierarchisches Clustering) und segmentiere die Kunden in 3–5 Gruppen.
- Beschreibe jedes Segment anhand von Schlüsselmerkmalen (Alter, Einkommen, Kaufverhalten usw.).

Ergebnisse visualisieren
- Erstelle geeignete Diagramme (z. B. Streudiagramme, Balkendiagramme oder Heatmaps), um die Kundensegmente zu visualisieren.
- Diskutiere die Ergebnisse: Was sind die charakteristischen Merkmale der einzelnen Segmente? Wie könnte das Unternehmen diese Informationen nutzen?


# Teil 2: Umsatzprognose

Zielvariable definieren
- Verwende den vorhandenen Datensatz, um eine Zielvariable zu erstellen, die den Umsatz des Kunden für die nächsten 30 Tage vorhersagt.

Modelltraining
- Teile die Daten in Trainings- und Testdaten auf.
- Trainiere mindestens zwei verschiedene Modelle (z. B. lineare Regression, Entscheidungsbaum, Random Forest oder XGBoost), um den zukünftigen Umsatz zu prognostizieren.
- Verwende geeignete Metriken (z. B. RMSE, MAE), um die Leistung der Modelle zu bewerten.

Modellbewertung
- Diskutiere, welches Modell am besten funktioniert und warum. Gibt es Merkmale, die besonders stark zum Modell beitragen?


# Teil 3 (Optional): Churn-Analyse

Abwanderungsmodell
- Verwende den vorhandenen Churn-Indikator (label_churn), um ein Modell zur Vorhersage der Kundenabwanderung zu trainieren (z. B. Logistic Regression, Random Forest).
- Diskutiere, welche Merkmale am wichtigsten sind, um die Abwanderung eines Kunden vorherzusagen.
- Stelle mögliche Maßnahmen vor, die das Unternehmen ergreifen könnte, um die Abwanderung zu verhindern.

Anforderungen
- Kommentiere deinen Code klar und verständlich.
- Verwende bewährte Methoden zur Datenaufbereitung und -modellierung.
- Visualisiere deine Ergebnisse in einer gut verständlichen und ansprechenden Weise.
- Schreibe einen kurzen Bericht (Markdown, Jupyter Notebook oder als separaten Text), in dem du deine Herangehensweise, die Modelle und die Ergebnisse erklärst.


Technische Voraussetzungen
- Du kannst eine beliebige Programmiersprache oder ein Framework verwenden, aber Python (mit Pandas, Scikit-Learn, Matplotlib/Seaborn) wird bevorzugt.
- Du solltest deine Ergebnisse in einem Jupyter Notebook oder einer ähnlichen Umgebung präsentieren.

# Bewertungskriterien

Datenaufbereitung                
- Wie gut und sauber hast du die Daten aufbereitet und mögliche Probleme gelöst? 

Modellleistung                   
- Wie gut sind deine Modelle und wie gründlich hast du sie evaluiert?  

Segmentierung                    
- Wie sinnvoll und interpretierbar sind die Kundensegmente?    

Visualisierung und Kommunikation  
- Wie gut hast du deine Ergebnisse visuell dargestellt und erklärt? 

Dokumentation                     
- Ist der Code klar kommentiert und die Vorgehensweise gut beschrieben?          
 