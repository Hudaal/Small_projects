import matplotlib.pyplot as plt
from EnkeltSpill import EnkeltSpill
from Spiller import Spiller


def call_husk(valg):
    if valg == '4':
        husk = int(input("Hvor mange steg vil du huske? "))
    else:
        husk = 1
    return husk


class MangeSpill:
    def __init__(self, spiller1, spiller2, antll_spill):
        self.enkelt_spill = EnkeltSpill(spiller1, spiller2)
        self.ganger = antll_spill

    def arranger_turnering2(self):
        i = 1
        while i <= self.ganger:
            print("\n\nRunde: {}\n".format(i))
            print("1. Tilfeldig valg\n"
                  "2. Sekvens valg\n"
                  "3. Mestvanlig\n"
                  "4. Historiker\n")
            s1_valg = input("Spiller 1: ")
            husk1 = call_husk(s1_valg)
            s2_valg = input("Spiller 2: ")
            husk2 = call_husk(s2_valg)
            self.enkelt_spill.gjennomfoer_spill(s1_valg, s2_valg, husk1, husk2)
            print(self.enkelt_spill)
            self.enkelt_spill.spiller1.prosent.append(
                self.enkelt_spill.spiller1.poeng / i)
            self.enkelt_spill.spiller2.prosent.append(
                self.enkelt_spill.spiller2.poeng / i)
            i += 1

    def arranger_turnering(self, s1_valg, s2_valg, husk1, husk2):
        i = 1
        while i <= self.ganger:
            #s1_valg = input("Spiller 1: ")
            #husk1 = call_husk(s1_valg)
            #s2_valg = input("Spiller 2: ")
            #husk2 = call_husk(s2_valg)
            self.enkelt_spill.gjennomfoer_spill(s1_valg, s2_valg, husk1, husk2)
            # print(self.enkelt_spill)
            self.enkelt_spill.spiller1.prosent.append(
                self.enkelt_spill.spiller1.poeng / i)
            self.enkelt_spill.spiller2.prosent.append(
                self.enkelt_spill.spiller2.poeng / i)
            i += 1

    def __str__(self):
        return "Til sammen har {} {} poeng, og har {} {} poeng.".format(
            self.enkelt_spill.spiller1.name,
            self.enkelt_spill.spiller1.poeng,
            self.enkelt_spill.spiller2.name,
            self.enkelt_spill.spiller2.poeng) + "\n\nVinneren er {}".format(self.vinner())

    def vinner(self):
        if self.enkelt_spill.spiller1.poeng > self.enkelt_spill.spiller2.poeng:
            return self.enkelt_spill.spiller1.name
        return self.enkelt_spill.spiller2.name

    def plot_graph(self):
        all_times = range(self.ganger + 1)
        spiller2 = self.enkelt_spill.spiller2.prosent
        spiller1 = self.enkelt_spill.spiller1.prosent
        plt.plot(all_times, spiller1)
        plt.plot(all_times, spiller2)
        plt.show()


def main():
    spiller1 = Spiller()
    spiller2 = Spiller()
    # spiller1.oppgi_navn("Huda")
    #spiller2.oppgi_navn("Muhammad Kheir")
    spiller1.oppgi_navn(input("1) Hva heter du? "))
    spiller2.oppgi_navn(input("2) Hva heter du? "))
    spill = MangeSpill(spiller1, spiller2, int(
        input("Hvor mange ganger vil dere spille? ")))
    print("{} Hvordan vil du spille? ".format(spiller1.name))
    print("1. Tilfeldig valg\n"
          "2. Sekvens valg\n"
          "3. Mestvanlig\n"
          "4. Historiker\n")
    s1_valg = input("...")
    husk1 = call_husk(s1_valg)
    print("{} Hvordan vil du spille? ".format(spiller2.name))
    s2_valg = input("...")
    husk2 = call_husk(s2_valg)
    spill.arranger_turnering(s1_valg, s2_valg, husk1, husk2)
    print(spill)
    spill.plot_graph()


main()
