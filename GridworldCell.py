class GridworldCell:
    def __init__(self, id):
        self.id = id
        self.fill = None

    def is_filled(self):
        return self.fill != None

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return str(self.id)
