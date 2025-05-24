class Kandidaat:
    def __init__(self, naam):
        self.naam = naam
        self.stemmen = []

    def geef_stem(self, stem):
        self.stemmen.append(stem)

    def __str__(self):
        return f"{self.naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self.kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self.kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self.naam = naam


    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} heeft gestemd op {kandidaat}")

class Verkiezing:
    def __init__(self):
        self.kandidaten = []
        self.kiezers = []

    def voeg_kandidaat_toe(self, kandidaat):
        self.kandidaten.append(kandidaat)

    def voeg_kiezer_toe(self, kiezer):
        self.kiezers.append(kiezer)

    def stemronde(self):
        for kiezer in self.kiezers:
            kiezer.stem(self.kandidaten[0])