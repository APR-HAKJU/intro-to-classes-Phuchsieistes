# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""
class buch:
    def __init__(self,titel,autor,seiten,gelesen):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesen = gelesen

buch1 = buch("HarryPotter", "JK Rowling", 300, False)
buch2 = buch("Das Leben von TheLenzi", "TheLenzi", 500, True)

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.
print(f"{buch1.titel} habe ich gelesen: {buch1.gelesen}")
print(f"{buch2.titel} habe ich gelesen: {buch2.gelesen}")