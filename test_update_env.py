from main import UpdateEnv

def test_env_exists():
    test_env = [[1, 1],[1, 1]]
    env = UpdateEnv(test_env).current_env()
    assert env == test_env

def test_env_size():
    test_env = [[1, 1],[1, 1],[1, 1]]
    test_m, test_n = UpdateEnv(test_env).env_size()
    assert test_m == len(test_env) and test_n == len(test_env[0])
