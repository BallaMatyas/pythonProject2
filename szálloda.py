from abc import ABC, abstractmethod
from datetime import datetime


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalt_datumok = set()

    @abstractmethod
    def get_szoba_tipus(self):
        pass

    def foglal(self, datum):
        if datum not in self.foglalt_datumok:
            self.foglalt_datumok.add(datum)
            return self.ar
        else:
            return 0

    def lemond(self, datum):
        if datum in self.foglalt_datumok:
            self.foglalt_datumok.remove(datum)
            return self.ar
        else:
            return 0


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 85000)

    def get_szoba_tipus(self):
        return "Egyágyas szoba"


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 150000)

    def get_szoba_tipus(self):
        return "Kétágyas szoba"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                ar = szoba.foglal(datum)
                if ar != 0:
                    foglalas = Foglalas(szoba, datum, ar)
                    return foglalas
                else:
                    return None
        return None

    def lemondas(self, foglalas):
        szoba = foglalas.szoba
        ar = szoba.lemond(foglalas.datum)
        if ar != 0:
            return ar
        else:
            return None

    def listaz_foglalasok(self):
        for szoba in self.szobak:
            for datum in szoba.foglalt_datumok:
                foglalas = Foglalas(szoba, datum, szoba.ar)
                print(f"Foglalás: {foglalas.get_foglalas()}")


class Foglalas:
    def __init__(self, szoba, datum, ar):
        self.szoba = szoba
        self.datum = datum
        self.ar = ar

    def get_foglalas(self):
        return f"{self.szoba.get_szoba_tipus()} foglalva {self.datum.date()} napra, ára: {self.ar} Ft"


egyagyas = EgyagyasSzoba(101)
ketagyas = KetagyasSzoba(201)

szalloda = Szalloda("Danubius Hotel")
szalloda.add_szoba(egyagyas)
szalloda.add_szoba(ketagyas)


foglalas1 = szalloda.foglalas(101, datetime(2023, 12, 1))
foglalas2 = szalloda.foglalas(201, datetime(2023, 12, 2))


foglalas3 = szalloda.foglalas(101, datetime(2023, 12, 3))
szalloda.lemondas(foglalas3)


szalloda.listaz_foglalasok()
