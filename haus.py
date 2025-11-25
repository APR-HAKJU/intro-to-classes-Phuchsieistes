# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self,quadratmeter,schlafzimmer,badezimmer):
        self.quadratmeter = quadratmeter
        self.schalfzimmer = schlafzimmer
        self.badezimmer = badezimmer

haus1 = Haus(120,2,3)


print(f"Haus: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.
haus2 = Haus(200,4,4)
haus3 = Haus(120,1,10)
haus4 = Haus(100,2,1)

# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.
print(f"{haus2.schlafzimmer}und{haus2.badezimmer}")
print(f"{haus3.schlafzimmer}und{haus3.badezimmer}")
print(f"{haus4.schlafzimmer}und{haus4.badezimmer}")