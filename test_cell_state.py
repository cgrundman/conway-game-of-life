# from unittest import TestCase

# class TryTesting(TestCase):
#     def test_always_passes(self):
#         self.assertTrue(True)

#     def test_always_fails(self):
#         self.assertTrue(False)

from main import CellStateCheck

def test_cell_exists():
    cell = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert cell.whole_community()