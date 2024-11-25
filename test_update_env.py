from update_env import UpdateEnv

def test_return_current_env():
    test_env = [[1, 1],[1, 1]]
    environment = UpdateEnv(test_env)
    assert environment.return_current_env() == test_env

def test_calc_env_size():
    test_env = [[1, 1],[1, 1],[1, 1]]
    environment = UpdateEnv(test_env)
    m, n = environment.calc_env_size()
    assert m == len(test_env) and n == len(test_env[0])

def test_pad_environment():
    test_env = [[1, 2],
                [3, 4],
                [5, 6]]
    test_env_padded = [[0, 0, 0, 0], 
                       [0, 1, 2, 0], 
                       [0, 3, 4, 0], 
                       [0, 5, 6, 0], 
                       [0, 0, 0, 0]]
    environment = UpdateEnv(test_env)
    assert environment.pad_environment() == test_env_padded

def test_extract_neighborhood():
    test_env = [[1, 2],
                [3, 4],
                [5, 6]]
    test_neighborhood = [[3, 4, 0],
                         [5, 6, 0],
                         [0, 0, 0]]
    environment = UpdateEnv(test_env)
    assert environment.extract_neighborhood() == test_neighborhood

def test_iterate_through_environment():
    test_env = [[1, 2],
                [3, 4],
                [5, 6]]
    iteration_order = [1, 2, 3, 4, 5, 6]
    environment = UpdateEnv(test_env)
    assert environment.iterate_through_environment() == iteration_order

def test_update_env_1x1():
    test_env = [[1]]
    updated_env = UpdateEnv(test_env)
    assert updated_env.update_environment() == [[0]]

def test_update_env_2x3():
    test_env = [[1, 1],
                [1, 0],
                [1, 0]]
    updated_env = UpdateEnv(test_env)
    assert updated_env.update_environment() == [[1, 1],[1, 0],[0, 0]]

def test_update_env_5x5():
    test_env = [[1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 0, 0, 0]]
    test_sol = [[1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 1, 0, 0],
                [1, 0, 1, 0, 0]]
    updated_env = UpdateEnv(test_env)
    assert updated_env.update_environment() == test_sol