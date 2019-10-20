class Ability:

    # Class variables
    #
    name = ""
    range = 0
    cell = 0
    ap = 0
    dmg = 0

    def __init__(self, name, rang, cell, ap, dam):
        self.name = name
        self.range = rang
        self.cell = cell
        self.ap = ap
        self.dmg = dam

