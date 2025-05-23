# decaan_verkiezing.py
from verkiezing import Kandidaat, Stem, Kiezer, Verkiezing


class DecaanKandidaat(Kandidaat):
    def __init__(self, naam: str, opleiding: str):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self) -> str:
        return f"{self.naam} ({self.opleiding})"


class DecaanStem(Stem):
    def __init__(self, kandidaat: DecaanKandidaat):
        super().__init__(kandidaat)
        # extra info niet nodig; zit al in kandidaat


class DecaanKiezer(Kiezer):
    def __init__(self, naam: str, opleiding: str):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat: DecaanKandidaat) -> None:
        """Een kiezer mag alleen stemmen op kandidaten van zijn/haar eigen opleiding."""
        if kandidaat.opleiding != self.opleiding:
            print(f"{self.naam} mag niet stemmen op {kandidaat}")
            return
        stem = DecaanStem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} stemt op {kandidaat}")


class DecaanVerkiezing(Verkiezing):
    """Concrete verkiezing; hier kunnen in de toekomst extra regels komen."""
    pass


# even testje doen
if __name__ == "__main__":
    verkiezing = DecaanVerkiezing()

    # kandidaten
    kandidaten = [
        DecaanKandidaat("Jan",   "Wiskunde"),
        DecaanKandidaat("Piet",  "Natuurkunde"),
        DecaanKandidaat("Klaas", "Scheikunde"),
        DecaanKandidaat("Marie", "Biologie"),
        DecaanKandidaat("Anna",  "Informatica"),
    ]
    for k in kandidaten:
        verkiezing.voeg_kandidaat_toe(k)

    
    kiezers = [
        DecaanKiezer("Henk", "Wiskunde"),
        DecaanKiezer("Els",  "Natuurkunde"),
        DecaanKiezer("Bob",  "Informatica"),
    ]
    for kz in kiezers:
        verkiezing.voeg_kiezer_toe(kz)

    # elke kiezer probeert op alle kandidaten te stemmen
    for kz in verkiezing.kiezers:
        for k in verkiezing.kandidaten:
            kz.stem(k)

    verkiezing.resultaten()
