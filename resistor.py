from math import ceil
from decimal import Decimal

class Resistor(object):

    def __init__(self, bands = ['n', 'b', 'n', 'l'], nodep = 0):
        super(Resistor, self).__init__()

        values = [
            {"b": 0,"n": 1,"r": 2,"o": 3,"y": 4,"g": 5,"l": 6,"p": 7,"t": 8,"w": 9,"d": -1,"s": -2},
            {"n": 1,"r": 2,"g": 0.5,"l": 0.25,"p": 0.1,"t": 0.05,"d": 5,"s": 10},
            {"n": 100, "r": 50, "o": 15, "y": 25, "l": 10, "p": 5}
            ]

        self.n_bands = len(bands)
        self.bands = bands

        # For resistors with 4 bands:
        self.band0 = bands[0]
        self.band1 = bands[1]
        self.band2 = bands[2]
        self.band3 = bands[3]

        self.h = int(ceil(self.n_bands / 2))
        self.digits = int(''. join([str(values[0][n]) for n in self.bands[:self.h]]))
        self.multiplier = values[0][self.bands[self.h]]
        self.value = self.digits * 10 ** self.multiplier
        self.tolerance = values[1][self.bands[self.h + 1]]

        # For resistors with 5 bands.
        self.band4 = bands[4] if self.n_bands >= 5 else None

        # For resistors with 6 bands.
        self.band5 = bands[5] if self.n_bands == 6 else None
        self.tcr = values[2][self.h + 2] if self.n_bands == 6 else None


    def __str__(self):
        return str(self.value) + ' ohm'


    def ohms(self):
        return str(self.value) + ' ohm'


    def kiloohms(self):
        return str(self.value / 1000) + ' kiloohm'


    def megaohms(self):
        return str(self.value / 1000000) + ' megaohm'


    def sci_notation(self):
        output = '%.2E' % Decimal(self.value)
        output = output.split('E')
        output[1] = str(int(output[1]))
        return 'x10?'.join(output)


    def tolerance_pt(self):
        return '+-' + str(self.tolerance) + ' %'


    def tolerance_ohms(self):
        return '+-' + str((self.tolerance / 100) * self.value) + ' ohm'


    def tcr_ppt(self):
        return str(self.tolerance * self.value) + ' ppt'


    def full_form(self):
        return [
            [self.ohms(), self.kiloohms(), self.megaohms(), self.sci_notation()],
            [self.tolerance_pt(), self.tolerance_ohms()],
            self.tcr]
