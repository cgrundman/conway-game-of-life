from cell_state import CellStateCheck

class UpdateEnv():
    def __init__(self, env):
        # Create Environment
        self.environment = env

        # Create new environment variable
        self.new_environment = env
        print(len(self.new_environment))
        print(len(self.new_environment[0]))

        # Extract size of the environment
        self.env_size()

        # Pad the Environment
        self.env_w_padding()

        # Create neighborhood
        self.neighborhood = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        # Iterate through padded environment
        for row_idx in range(len(self.environment_padded)-2):
            for col_idx in range(len(self.environment_padded[row_idx])-2):
                # Set current neighborhood values
                for n_x in range(len(self.neighborhood)):
                    for n_y in range(len(self.neighborhood[n_x])):
                        self.neighborhood[n_x][n_y] = self.environment_padded[row_idx+n_x][col_idx+n_y]
                # Find new value of environment
                print("Environment_pad:")
                for row in  self.environment_padded:
                    print(row)
                print(f"Current cell: {self.environment_padded[row_idx+1][col_idx+1]}")
                print(f"Neighborhood: {self.neighborhood}")
                # new_cell_state = CellStateCheck(self.neighborhood).new_cell_state()
                self.new_environment[row_idx][col_idx] = CellStateCheck(self.neighborhood).new_cell_state()
                # print(f"Neighborhood: {self.neighborhood}")


        self.neighborhood = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        loc = [1, 1]
        for idx_m, row in enumerate(self.neighborhood):
            for idx_n in range(len(row)):
                self.neighborhood[idx_m][idx_n] = self.environment_padded[loc[0] + idx_m - 1][loc[1] + idx_n -1]

        return None
    
    def current_env(self):
        return self.environment

    def env_size(self):
        self.m, self.n = len(self.environment), len(self.environment[0])
        return self.m, self.n
    
    def env_w_padding(self):
        self.environment_padded = self.environment
        for idx, row in enumerate(self.environment_padded): # reduce by removing enumerate
            self.environment_padded[idx].insert(0, 0)
            self.environment_padded[idx].append(0)
        self.environment_padded.insert(0, [0] * (self.n + 2))
        self.environment_padded.append([0] * (self.n + 2))
        return self.environment_padded
    
    def extract_neighborhood(self):
        self.neighborhood = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        loc = [1, 1]
        for idx_m, row in enumerate(self.neighborhood):
            for idx_n in range(len(row)):
                self.neighborhood[idx_m][idx_n] = self.environment_padded[loc[0] + idx_m - 1][loc[1] + idx_n -1]
        return self.neighborhood
    
    def env_iteration(self):
        iteration_list = []
        for row_idx in range(len(self.environment_padded)-2):
            for col_idx in range(len(self.environment_padded[row_idx])-2):
                iteration_list.append(self.environment_padded[row_idx + 1][col_idx + 1])
        return iteration_list
    
    def update_env(self):
        return self.new_environment