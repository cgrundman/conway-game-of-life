from cell_state import CellStateCheck

class UpdateEnv():
    def __init__(self, env):
        self.environment = env
        self.m, self.n = len(self.environment), len(self.environment[0])

        return None
    
    def current_env(self):
        return self.environment

    def env_size(self):
        return self.m, self.n