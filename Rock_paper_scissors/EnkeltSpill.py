"""Et enkelt spill"""

from Aksjon import Aksjon
from Spiller import Spiller

class EnkeltSpill:
    def __init__(self, s1, s2):
        self.spiller1 = s1
        self.spiller2 = s2
        self.spiller1.add_spiller(self.spiller2)
        self.spiller2.add_spiller(self.spiller1)

    def gjennomfoer_spill(self, s1_valg, s2_valg, husk1, husk2):
        self.spiller1.velg_aksjon(s1_valg, husk1)
        self.spiller2.velg_aksjon(s2_valg, husk2)
        aksjon1 = Aksjon(self.spiller1.valg)
        aksjon2 = Aksjon(self.spiller2.valg)
        poeng1 = 0
        poeng2 = 0
        if aksjon1 == aksjon2:
            poeng1 = poeng2 = 1
        elif aksjon1 > aksjon2:
            poeng1 = 1
        else:
            poeng2 = 1
        self.spiller1.motta_resultat(poeng1)
        self.spiller2.motta_resultat(poeng2)

    def __str__(self):
        string_valg = "{} har valgt {}.\nOg {} har valgt {}" .format(
            self.spiller1.name, self.spiller1.valg, self.spiller2.name, self.spiller2.valg)
        string_poeng = "{} har {} poeng.\nOg {} har {} poeng." .format(
            self.spiller1.name,
            self.spiller1.resultat,
            self.spiller2.name,
            self.spiller2.resultat)
        return string_valg + "\n" + string_poeng