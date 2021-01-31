from Tilfeldig import Tilfeldig


class Historiker:
    def __init__(self, spiller, husk):
        self.husk = husk
        self.spiller = spiller
        self.tilfeldig = Tilfeldig(self.spiller)

    def historiker(self):
        """Hoved funksjon"""
        if len(self.spiller.mot_spill) == 0:
            return self.tilfeldig.tilfeldig()
        new_array = []
        next_array = []
        try:
            for i in range(self.husk, 0, -1):
                new_array.append(self.spiller.mot_spill[-i])
        except BaseException:
            return self.tilfeldig.tilfeldig()

        if len(new_array) == 0:
            return self.tilfeldig.tilfeldig()

        # check how many steps to go forward
        if self.husk == 1:
            forward = 1
        else:
            forward = self.husk - 1

        for i in range(0, len(self.spiller.mot_spill) - self.husk, forward):
            count = 0
            while self.spiller.mot_spill[i + count] == new_array[count]:
                # print("arr: {}".format(new_array[count]))
                count += 1
                if count == self.husk:
                    break
            if count == self.husk:
                try:
                    # print("next one: {}".format(array[i+count]))
                    next_array.append(self.spiller.mot_spill[i + count])
                except Exception:
                    print("This is the last item!")

        times_repeated = self.most_repeated(next_array)
        if self.all_zero(times_repeated):
            return self.tilfeldig.tilfeldig()
        return self.spiller.whichBetter(
            self.spiller.all_valg[times_repeated.index(max(times_repeated))])

    def most_repeated(self, array):
        times = []
        for ele in self.spiller.all_valg:
            count = 0
            for ele2 in array:
                if ele == ele2:
                    count += 1
            times.append(count)
        return times

    def all_zero(self, array):
        count = 0
        for ele in array:
            if ele == 0:
                count += 1
        if count == len(array):
            return True
        return False
