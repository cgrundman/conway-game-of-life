from cell_state import CellStateCheck

class UpdateEnv():
    def __init__(self, env):
        # Create Environment
        self.environment = list(env)

        # Extract size of the environment
        self.calc_env_size()

        # Create Padded Environment
        padded = list(env)
        padded.insert(0, [0] * (self.n))
        padded.append([0] * (self.n))
        for idx in range(len(padded)):
            padded[idx].insert(0, 0)
            padded[idx].append(0)
        self.environment_padded = list(padded)

        # Create new environment variable
        self.new_environment = []

        # Set blank neighborhood
        self.neighborhood = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        # Iterate through padded environment
        for row_idx in range(len(self.environment_padded)-2):
            self.new_environment_row = []
            for col_idx in range(len(self.environment_padded[row_idx])-2):
                # Set current neighborhood values
                for n_x in range(len(self.neighborhood)):
                    for n_y in range(len(self.neighborhood[n_x])):
                        self.neighborhood[n_x][n_y] = self.environment_padded[row_idx+n_x][col_idx+n_y]
                self.new_cell_state = CellStateCheck(self.neighborhood).new_cell_state()
                self.new_environment_row.append(self.new_cell_state)
            self.new_environment.append(self.new_environment_row)

        return None
    
    def return_current_env(self):
        return self.environment

    def calc_env_size(self):
        self.m, self.n = len(self.environment), len(self.environment[0])
        return self.m, self.n
    
    def pad_environment(self):
        return self.environment_padded
    
    def extract_neighborhood(self):
        return self.neighborhood
    
    def iterate_through_environment(self):
        iteration_list = []
        for row_idx in range(len(self.environment_padded)-2):
            for col_idx in range(len(self.environment_padded[row_idx])-2):
                iteration_list.append(self.environment_padded[row_idx + 1][col_idx + 1])
        return iteration_list
    
    def update_environment(self):
        return self.new_environment