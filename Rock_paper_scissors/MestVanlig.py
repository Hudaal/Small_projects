"""
Det mest vanlig valget.
"""

class MestVanlig:
    def __init__(self, spiller):
        self.spiller = spiller

    def mest_vanlig(self):
        """Hoved metode"""
        counts = [
            self.calculate_times("Stein"),
            self.calculate_times("Saks"),
            self.calculate_times("Papir")]
        return self.spiller.whichBetter(
            self.spiller.all_valg[counts.index(max(counts))])

    def calculate_times(self, type_valg):
        """check how many times has been repeated"""
        count = 0
        for item in self.spiller.mot_spill:
            if item == type_valg:
                count += 1
        return count

    def __str__(self):
        return self.spiller.valg
