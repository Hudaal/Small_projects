"""Rekke følge: Stein, Saks, Papir"""

class Sekvensiell:
    """sekvensiell klasse"""
    def __init__(self, spiller):
        self.spiller = spiller

    def sekvensiell(self):
        """Hover metode"""
        if self.spiller.sekvens_teller >= 2:
            self.spiller.sekvens_teller = 0
        else:
            self.spiller.sekvens_teller += 1
        return self.spiller.all_valg[self.spiller.sekvens_teller]
