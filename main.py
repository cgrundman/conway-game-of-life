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
        self.cell = self.community[1][1]

        # Extract Neighborhood
        self.neighborhood = []
        for idx_x, row in enumerate(self.community):
            for idx_y, col in enumerate(row):
                if idx_x == 1 and idx_y == 1:
                    pass
                else:
                    self.neighborhood.append(row[col])

        self.neighborhood_sum = sum(self.neighborhood)

        return None
    
    def whole_community(self):
        return self.community
    
    def cell_only(self):
        return self.cell
    
    def neighborhood_only(self):
        return self.neighborhood
    
    def neighborhood_value(self):
        return self.neighborhood_sum


if __name__ == "__main__":
    print("Groovy")