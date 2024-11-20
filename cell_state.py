# Game of Life

# wikipedia page: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life 

# Rules:
# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

class CellStateCheck():
    def __init__(self, community):
        self.community = community

        # Extract Cell
        self.cell_only()

        # Extract neighborhood value
        self.neighborhood_value()

        # Return new cell state
        self.new_cell_state()
        
        return None
    
    def whole_community(self):
        return self.community
    
    def cell_only(self):
        self.cell = self.community[1][1]
        return self.cell
    
    def neighborhood_only(self):
        self.neighborhood = []
        for row in range(len(self.community)):
            for col in range(len(self.community[row])):
                if row == 1 and col == 1:
                    pass
                else:
                    self.neighborhood.append(self.community[row][col])
        return self.neighborhood
    
    def neighborhood_value(self):
        # Extract Neighborhood
        neighborhood = self.neighborhood_only()
        self.neighborhood_sum = sum(neighborhood)
        return self.neighborhood_sum
    
    def new_cell_state(self):
        # Test live cell state
        # Die if not enough neighbors
        if self.cell == 1 and self.neighborhood_sum < 2:
            self.new_cell = 0
        # Die if too many neighbors
        elif self.cell == 1 and self.neighborhood_sum > 3:
            self.new_cell = 0
        # Birth if 3 neighbors
        elif self.cell == 0 and self.neighborhood_sum == 3:
            self.new_cell = 1
        # Retain cell state
        else:
            self.new_cell = self.cell
        return self.new_cell


if __name__ == "__main__":
    community = [[1, 0, 0],[1, 0, 0],[0, 0, 0]]
    print(f"Cell state: {CellStateCheck(community).cell_only()}")
    print(f"Neighborhood value: {CellStateCheck(community).neighborhood_value()}")
    print(f"New cell state: {CellStateCheck(community).new_cell_state()}")