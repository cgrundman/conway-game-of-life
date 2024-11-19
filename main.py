from cell_state import CellStateCheck

class UpdateEnv():
    def __init__(self, env):
        # Create Environment
        self.environment = env

        # Extract size of the environment
        self.m, self.n = len(self.environment), len(self.environment[0])

        # Pad the Environment
        self.environment_padded = self.environment
        for idx, row in enumerate(self.environment_padded):
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