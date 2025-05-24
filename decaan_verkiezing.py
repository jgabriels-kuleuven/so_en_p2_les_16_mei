from verkiezing import Kandidaat, Stem, Kiezer, Verkiezing

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

class DecaanVerkiezing(Verkiezing):
    def stemronde(self):
        for kiezer in self.kiezers:
            for kandidaat in self.kandidaten:
                if hasattr(kandidaat, "opleiding") and hasattr(kiezer, "opleiding"):
                    if kandidaat.opleiding == kiezer.opleiding:
                        kiezer.stem(kandidaat)
                        break

verkiezing2020 = DecaanVerkiezing()

verkiezing2020.voeg_kandidaat_toe(DecaanKandidaat("Jan", "Informatica"))
verkiezing2020.voeg_kandidaat_toe(DecaanKandidaat("Piet", "Wiskunde"))
verkiezing2020.voeg_kandidaat_toe(DecaanKandidaat("Ines", "Informatica"))

verkiezing2020.voeg_kiezer_toe(DecaanKiezer("Sara", "Informatica"))
verkiezing2020.voeg_kiezer_toe(DecaanKiezer("Tom", "Wiskunde"))
verkiezing2020.voeg_kiezer_toe(DecaanKiezer("Anna", "Informatica"))

verkiezing2020.stemronde()

print("verkiezingsresultaten")
for kandidaat in verkiezing2020.kandidaten:
    print(kandidaat, len(kandidaat.stemmen))