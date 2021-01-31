"""Spiller klasse og metoder"""

from Tilfeldig import Tilfeldig
from Sekvensiell import Sekvensiell
from Historiker import Historiker
from MestVanlig import MestVanlig


class Spiller:
    all_valg = ["Stein", "Saks", "Papir"]

    def __init__(self):
        self.resultat = 0
        self.valg = ""
        self.min_spill = []
        self.mot_spill = []
        self.name = "spillerx"
        self.sekvens_teller = 0
        self.mot_spiller = self
        self.poeng = 0
        self.prosent = [0.0]

    def velg_aksjon(self, valg, husk):
        """valg her mellom 1 til 4 for å velge metoden til valg"""
        if valg == '1':
            # print("tilfeldig******************")
            tilfeldig = Tilfeldig(self)
            self.valg = tilfeldig.tilfeldig()
        elif valg == '2':
            # print("sekv******************")
            sekvensiell = Sekvensiell(self)
            self.valg = sekvensiell.sekvensiell()
        elif valg == '3':
            # print("mest******************")
            mest_vanlig = MestVanlig(self)
            self.valg = mest_vanlig.mest_vanlig()
        else:
            # print("histro******************")
            hist = Historiker(self, husk)
            self.valg = hist.historiker()
        self.add_valg(self.valg)

    def motta_resultat(self, poeng):
        """Beregne poeng"""
        self.resultat = poeng
        self.poeng += poeng

    def oppgi_navn(self, name):
        self.name = "spiller {}".format(name)

    def add_valg(self, valg):
        self.min_spill.append(valg)
        self.mot_spiller.mot_spiller_change(valg)
        self.sekvens_teller = self.all_valg.index(valg)
        # print(valg)

    def mot_spiller_change(self, valg):
        self.mot_spill.append(valg)

    def add_spiller(self, spiller):
        self.mot_spiller = spiller

    def whichBetter(self, type_valg):
        """This function gives the stronger move"""
        word = ""
        if type_valg == "Stein":
            word = "Papir"
        elif type_valg == "Saks":
            word = "Stein"
        else:
            word = "Saks"
        return word
