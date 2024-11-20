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
        self.m, self.n = len(self.environment), len(self.environment[0])

        # Pad the Environment
        self.environment_padded = env
        for idx, row in enumerate(self.environment_padded): # reduce by removing enumerate
            self.environment_padded[idx].insert(0, 0)
            self.environment_padded[idx].append(0)
        self.environment_padded.insert(0, [0] * (self.n + 2))
        self.environment_padded.append([0] * (self.n + 2))

        # Create neighborhood
        self.neighborhood = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        # Iterate through padded environment
        for row_idx in range(len(self.environment_padded)-2):
            for col_idx in range(len(self.environment_padded[row_idx])-2):
                # Set current neighborhood values
                for i in range(len(self.neighborhood)):
                    self.neighborhood[i] = self.environment_padded[row_idx+i:2]
                # print(self.environment_padded[row_idx + 1][col_idx + 1]) # important information
                # Find new value of environment
                self.new_environment[row_idx + 1][col_idx + 1] = CellStateCheck(self.neighborhood).new_cell_state()
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
        return len(self.environment), len(self.environment[0])
    
    def env_w_padding(self):
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