# Game of Life

# wikipedia page: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life 

# Rules:
# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

from update_env import UpdateEnv
import time

if __name__ == "__main__":
    
    print(chr(27) + "[2J")
    # environment = [[1, 1, 0, 0, 0, 0, 0, 1, 1],
    #                [1, 0, 0, 0, 0, 0, 0, 0, 1],
    #                [0, 0, 0, 1, 0, 1, 0, 0, 0],
    #                [0, 0, 1, 1, 0, 1, 1, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 1, 1, 0, 1, 1, 0, 0],
    #                [0, 0, 0, 1, 0, 1, 0, 0, 0],
    #                [1, 0, 0, 0, 0, 0, 0, 0, 1],
    #                [1, 1, 0, 0, 0, 0, 0, 1, 1],]
    # environment = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1, 0, 0, 0, 0],
    #                [0, 0, 0, 1, 1, 1, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0],]
    environment = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],]
    
    for row in environment:
        print(row)

    for i in range(50):
        time.sleep(0.5)
        print(chr(27) + "[2J")

        environment = UpdateEnv(environment).update_environment()

        for row in environment:
            print(row)

    pass