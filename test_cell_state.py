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