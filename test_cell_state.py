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
    assert community.neighborhood_value() == 4
