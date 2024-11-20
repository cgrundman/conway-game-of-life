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
        cell = self.cell_only()

        # Extract Neighborhood
        self.neighborhood = []
        for row in range(len(self.community)):
            for col in range(len(self.community[row])):
                if row == 1 and col == 1:
                    pass
                else:
                    self.neighborhood.append(self.community[row][col])

        # Extract neighborhood value
        self.neighborhood_sum = sum(self.neighborhood)
        # Test live cell state
        # Die if not enough neighbors
        if cell == 1 and self.neighborhood_sum < 2:
            self.new_cell = 0
        # Die if too many neighbors
        elif cell == 1 and self.neighborhood_sum > 3:
            self.new_cell = 0
        # Birth if 3 neighbors
        elif cell == 0 and self.neighborhood_sum == 3:
            self.new_cell = 1
        # Retain cell state
        else:
            self.new_cell = cell
        
        return None
    
    def whole_community(self):
        return self.community
    
    def cell_only(self):
        self.cell = self.community[1][1]
        return self.cell
    
    def neighborhood_only(self):
        return self.neighborhood
    
    def neighborhood_value(self):
        return self.neighborhood_sum
    
    def new_cell_state(self):
        return self.new_cell


if __name__ == "__main__":
    print("Groovy")

    community = [[1, 0, 0],[1, 0, 0],[0, 0, 0]]
    print(CellStateCheck(community).neighborhood_value())