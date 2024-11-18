# from unittest import TestCase

# class TryTesting(TestCase):
#     def test_always_passes(self):
#         self.assertTrue(True)

#     def test_always_fails(self):
#         self.assertTrue(False)

from main import CellStateCheck

def test_community_exists():
    community = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert community.whole_community()

def test_cell_exists():
    community = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert community.cell_only() == community.whole_community()[1][1]

def test_neighborhood_exists():
    community = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert len(community.neighborhood_only()) == 8

def test_neighborhood_value():
    test_community = [[1, 1, 1],[0, 1, 0],[0, 1, 0]]
    community = CellStateCheck(test_community)
    # Create value to test against
    test_neighborhood = []
    for idx_x, row in enumerate(test_community):
        for idx_y, col in enumerate(row):
            if idx_x == 1 and idx_y == 1:
                pass
            else:
                test_neighborhood.append(row[col])#
    test_value = sum(test_neighborhood)
    assert community.neighborhood_value() == test_value