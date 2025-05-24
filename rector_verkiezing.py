from verkiezing import Kandidaat, Stem, Kiezer, Verkiezing

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"
    
class RectorKiezer(Kiezer):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

        


class RectorVerkiezing(Verkiezing):
     def stemronde(self):
        for kiezer in self.kiezers:
            laatst_geldige_kandidaat = None
            for kandidaat in self.kandidaten:
                if kandidaat.faculteit != kiezer.faculteit:
                    laatst_geldige_kandidaat = kandidaat
            
            if laatst_geldige_kandidaat is not None:
                kiezer.stem(laatst_geldige_kandidaat)
            else:
                kiezer.stem(self.kandidaten[-1])

verkiezing2022 = RectorVerkiezing()

verkiezing2022.voeg_kandidaat_toe(RectorKandidaat("Jan", "Economie"))
verkiezing2022.voeg_kandidaat_toe(RectorKandidaat("Piet", "Wiskunde"))
verkiezing2022.voeg_kandidaat_toe(RectorKandidaat("Ines", "Informatica"))
verkiezing2022.voeg_kandidaat_toe(RectorKandidaat("Hans", "Rechten"))
verkiezing2022.voeg_kandidaat_toe(RectorKandidaat("Mark", "Geneeskunde"))

verkiezing2022.voeg_kiezer_toe(RectorKiezer("Sara", "Informatica"))
verkiezing2022.voeg_kiezer_toe(RectorKiezer("Tom", "Wiskunde"))
verkiezing2022.voeg_kiezer_toe(RectorKiezer("Anna", "Informatica"))
verkiezing2022.voeg_kiezer_toe(RectorKiezer("William", "Sociale Wetenschappen"))
verkiezing2022.voeg_kiezer_toe(RectorKiezer("Harry", "Talen"))
verkiezing2022.voeg_kiezer_toe(RectorKiezer("Bart", "Geschiedenis"))

verkiezing2022.stemronde()

print("Verkiezingsresultaten")
for kandidaat in verkiezing2022.kandidaten:
    print(kandidaat, len(kandidaat.stemmen))