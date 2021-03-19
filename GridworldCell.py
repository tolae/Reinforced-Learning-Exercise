class GridworldCell:
    def __init__(self, id):
        self.id = id
        self.fill = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def is_filled(self):
        return self.fill != None

    def get_adjacent_states(self):
        return [\
            self.up,\
            self.right,\
            self.down,\
            self.left\
        ]

    def __eq__(self, other):
        if other is None:
            return False
        return self.id == other.id

    def __str__(self):
        return str(self.id)
    
    def __hash__(self):
        return self.id
