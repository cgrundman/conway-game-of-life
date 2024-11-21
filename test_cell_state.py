from cell_state import CellStateCheck

def test_whole_community():
    community = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert community.whole_community()

def test_cell_only():
    community = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert community.cell_only() == community.whole_community()[1][1]

def test_neighborhood_only():
    community = CellStateCheck([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    assert len(community.neighborhood_only()) == 8

def test_neighborhood_value():
    test_community = [[1, 1, 1],[0, 1, 0],[0, 1, 0]]
    community = CellStateCheck(test_community)
    # Create value to test against
    assert community.neighborhood_value() == 4

def test_underpopulation_new_cell_state():
    test_community = [[1, 0, 0],[0, 1, 0],[0, 0, 0]]
    community = CellStateCheck(test_community)
    assert community.new_cell_state() == 0

def test_overpopulation_new_cell_state():
    test_community = [[1, 1, 1],[0, 1, 0],[0, 1, 0]]
    community = CellStateCheck(test_community)
    assert community.new_cell_state() == 0

def test_survival_new_cell_state():
    test_community = [[1, 1, 1],[0, 1, 0],[0, 0, 0]]
    community = CellStateCheck(test_community)
    assert community.new_cell_state() == 1

def test_birth_new_cell_state():
    test_community = [[1, 1, 1],[0, 0, 0],[0, 0, 0]]
    community = CellStateCheck(test_community)
    assert community.new_cell_state() == 1