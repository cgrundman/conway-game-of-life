from main import UpdateEnv

def test_current_env():
    test_env = [[1, 1],[1, 1]]
    env = UpdateEnv(test_env).current_env()
    assert env == test_env

def test_env_size():
    test_env = [[1, 1],[1, 1],[1, 1]]
    test_m, test_n = UpdateEnv(test_env).env_size()
    assert test_m == len(test_env) and test_n == len(test_env[0])

def test_env_w_padding():
    test_env = [[1, 2],[3, 4],[5, 6]]
    test_env_padded = [[0, 0, 0, 0],[0, 1, 2, 0],[0, 3, 4, 0],[0, 5, 6, 0],[0, 0, 0, 0]]
    env_padded = UpdateEnv(test_env).env_w_padding()
    assert env_padded == test_env_padded

def test_extract_neighborhood():
    test_env = [[1, 2],[3, 4],[5, 6]]
    test_neighborhood = [[0, 0, 0],[0, 1, 2],[0, 3, 4]]
    neighborhood = UpdateEnv(test_env).extract_neighborhood()
    assert test_neighborhood == neighborhood

def test_env_iteration():
    test_env = [[1, 2],[3, 4],[5, 6]]
    iteration_order = [1, 2, 3, 4, 5, 6]
    iteration_list = UpdateEnv(test_env).env_iteration()
    assert iteration_list == iteration_order

def test_update_env_1x1():
    test_env = [[1]]
    updated_env = UpdateEnv(test_env).update_env()
    # assert updated_env == [[0]]
    pass