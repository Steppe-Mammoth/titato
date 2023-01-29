from titato.core.table.combinations import CombBase, CombDefault
from titato.core.table.annotations import CombsTypeT

COMB: CombBase = CombDefault()


# GITHUB COPILOT made this function

# The function takes two sets of combos as input combs1: CombsType, combs2: CombsType
# check all cells in each combination in each set for equality
# Returns True if the sets are equal, False otherwise
def check_equal(combs1: CombsTypeT, combs2: CombsTypeT) -> bool:
    # Check that the number of combinations in each set is equal
    if len(combs1) != len(combs2):
        return False
    # Check that each combination in the first set is in the second
    for comb1 in combs1:
        # Check that each combination in the second set is in the first
        for comb2 in combs2:
            # Check that each cell in the first combination is in the second combination
            for cell1 in comb1:
                if cell1 not in comb2:
                    break
            else:
                # If we got to this place, the combinations are equal
                break
        else:
            # If we got to this place, the combination in the first set was not found in the second
            return False
    # If we got to this place, the sets are equal
    return True


def test_comb_3_3_3():
    expected_combs = (((0, 0), (0, 1), (0, 2)),
                      ((0, 0), (1, 0), (2, 0)),
                      ((0, 0), (1, 1), (2, 2)),
                      ((0, 1), (1, 1), (2, 1)),
                      ((0, 2), (1, 2), (2, 2)),
                      ((0, 2), (1, 1), (2, 0)),
                      ((1, 0), (1, 1), (1, 2)),
                      ((2, 0), (2, 1), (2, 2)))

    combs = COMB.get_combinations(3, 3, 3)
    assert check_equal(expected_combs, combs) is True


def test_comb_2_2_2():
    expected_combs = (((0, 0), (0, 1)),
                      ((1, 0), (1, 1)),
                      ((0, 0), (1, 0)),
                      ((0, 1), (1, 1)),
                      ((0, 1), (1, 0)),
                      ((0, 0), (1, 1)))

    combs = COMB.get_combinations(2, 2, 2)
    assert check_equal(expected_combs, combs) is True


def test_comb_5_5_4():
    expected_combs = (
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 1), (0, 2), (0, 3), (0, 4)),

        ((1, 0), (1, 1), (1, 2), (1, 3)),
        ((1, 1), (1, 2), (1, 3), (1, 4)),

        ((2, 0), (2, 1), (2, 2), (2, 3)),
        ((2, 1), (2, 2), (2, 3), (2, 4)),

        ((3, 0), (3, 1), (3, 2), (3, 3)),
        ((3, 1), (3, 2), (3, 3), (3, 4)),

        ((4, 0), (4, 1), (4, 2), (4, 3)),
        ((4, 1), (4, 2), (4, 3), (4, 4)),

        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((1, 0), (2, 0), (3, 0), (4, 0)),

        ((0, 1), (1, 1), (2, 1), (3, 1)),
        ((1, 1), (2, 1), (3, 1), (4, 1)),

        ((0, 2), (1, 2), (2, 2), (3, 2)),
        ((1, 2), (2, 2), (3, 2), (4, 2)),

        ((0, 3), (1, 3), (2, 3), (3, 3)),
        ((1, 3), (2, 3), (3, 3), (4, 3)),

        ((0, 4), (1, 4), (2, 4), (3, 4)),
        ((1, 4), (2, 4), (3, 4), (4, 4)),

        ((0, 0), (1, 1), (2, 2), (3, 3)),
        ((1, 1), (2, 2), (3, 3), (4, 4)),

        ((0, 4), (1, 3), (2, 2), (3, 1)),
        ((1, 3), (2, 2), (3, 1), (4, 0)),

        ((0, 1), (1, 2), (2, 3), (3, 4)),
        ((1, 0), (2, 1), (3, 2), (4, 3)),

        ((3, 0), (2, 1), (1, 2), (0, 3)),
        ((4, 1), (3, 2), (2, 3), (1, 4)))

    combs = COMB.get_combinations(5, 5, 4)
    assert check_equal(expected_combs, combs) is True
