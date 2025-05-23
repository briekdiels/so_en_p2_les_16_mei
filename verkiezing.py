# verkiezing.py
from abc import ABC, abstractmethod


class Kandidaat:
    """Basisklasse voor alle kandidaten."""
    def __init__(self, naam: str):
        self._naam = naam
        self._stemmen: list["Stem"] = []

    
    @property
    def naam(self) -> str:
        return self._naam

    @property
    def stemmen(self) -> tuple["Stem"]:
        """Read-only view: buitenstaanders kunnen de interne lijst niet wijzigen."""
        return tuple(self._stemmen)

    def aantal_stemmen(self) -> int:
        return len(self._stemmen)

    
    def geef_stem(self, stem: "Stem") -> None:
        self._stemmen.append(stem)

    
    def __str__(self) -> str:          
        return self._naam

    def __repr__(self) -> str:         # in debugger
        return f"Kandidaat({self._naam!r})"


class Stem:
    """Generieke stem; subklassen kunnen extra context opslaan."""
    def __init__(self, kandidaat: Kandidaat):
        self.kandidaat = kandidaat

    def __str__(self) -> str:
        return f"Stem op {self.kandidaat}"


class Kiezer(ABC):
    """Abstracte kiezer – concrete klassen moeten zelf de stem-logica invullen."""
    def __init__(self, naam: str):
        self.naam = naam

    @abstractmethod
    def stem(self, kandidaat: Kandidaat) -> None:   # verplicht te implementeren
        ...


class Verkiezing(ABC):
    """
    Gemeenschappelijke logica voor elke verkiezing.
    Concrete subklassen hoeven alleen hun eigen validatieregels te schrijven.
    """
    def __init__(self):
        self._kandidaten: list[Kandidaat] = []
        self._kiezers: list[Kiezer] = []

    
    @property
    def kandidaten(self) -> tuple[Kandidaat]:
        return tuple(self._kandidaten)

    @property
    def kiezers(self) -> tuple[Kiezer]:
        return tuple(self._kiezers)

    
    def voeg_kandidaat_toe(self, k: Kandidaat) -> None:
        self._kandidaten.append(k)

    def voeg_kiezer_toe(self, kz: Kiezer) -> None:
        self._kiezers.append(kz)

    def resultaten(self) -> None:
        """Print een eenvoudig overzicht."""
        print(f"\n=== Resultaten {self.__class__.__name__} ===")
        for k in self._kandidaten:
            print(f"{k.naam:<15} – {k.aantal_stemmen():>2} stemmen")
