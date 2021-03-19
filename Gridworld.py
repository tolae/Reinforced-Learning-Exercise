from GridworldCell import GridworldCell

class Gridworld:
    def __init__(self, debug=False):
        self._create_grid()
        self._connect_grid()
        if debug:
            self.print_grid()
    
    def _create_grid(self):
        self.grid = [[GridworldCell(row * 5 + col + 1) for col in range(5)] for row in range(5)]

    def _connect_grid(self):
        for row in range(5):
            for col in range(5):
                if row > 0:
                    self.grid[row][col].up = self.grid[row-1][col]
                if row < 4:
                    self.grid[row][col].down = self.grid[row+1][col]
                if col > 0:
                    self.grid[row][col].left = self.grid[row][col-1]
                if col < 4:
                    self.grid[row][col].right = self.grid[row][col+1]
    
    def print_grid(self):
        for row in range(5):
            print("")
            for col in range(5):
                if self.grid[row][col].is_filled():
                    print("*" + str(self.grid[row][col]) + "*", end="\t")
                else:
                    print(str(self.grid[row][col]), end="\t")
