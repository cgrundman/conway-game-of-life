class CellStateCheck():
    def __init__(self, community):
        self.community = community

        # Extract Cell
        self.return_cell_only()

        # Extract neighborhood value
        self.return_neighborhood_value()

        # Return new cell state
        self.return_new_cell_state()
        
        return None
    
    def return_community(self):
        return self.community
    
    def return_cell_only(self):
        self.cell = self.community[1][1]
        return self.cell
    
    def return_neighborhood_only(self):
        self.neighborhood = []
        for row in range(len(self.community)):
            for col in range(len(self.community[row])):
                if row == 1 and col == 1:
                    pass
                else:
                    self.neighborhood.append(self.community[row][col])
        return self.neighborhood
    
    def return_neighborhood_value(self):
        # Extract Neighborhood
        neighborhood = self.return_neighborhood_only()
        self.neighborhood_sum = sum(neighborhood)
        return self.neighborhood_sum
    
    def return_new_cell_state(self):
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