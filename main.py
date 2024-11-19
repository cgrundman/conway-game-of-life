from cell_state import CellStateCheck

class UpdateEnv():
    def __init__(self, env):
        # Create Environment
        self.environment = env

        # Extract size of the environment
        self.m, self.n = len(self.environment), len(self.environment[0])

        # Pad the Environment
        self.environment_padded = self.environment
        for idx, row in enumerate(self.environment_padded): # reduce by removing enumerate
            self.environment_padded[idx].insert(0, 0)
            self.environment_padded[idx].append(0)
        self.environment_padded.insert(0, [0] * (self.n + 2))
        self.environment_padded.append([0] * (self.n + 2))

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