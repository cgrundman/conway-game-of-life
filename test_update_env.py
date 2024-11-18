from main import UpdateEnv

def test_env_exists():
    test_env = [[1, 1],[1, 1]]
    env = UpdateEnv(test_env).current_env()
    assert env == test_env