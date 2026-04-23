

from largest_time import create_time, all_combs_of_four, check_if_time_valid, largest_time


# Tests that create_time correctly makes a time string from a list of four integers

def test_create_time_length():
    " Tests that create_time makes a string 5 characters long"
    assert len(create_time("1111")) == 5


def test_create_time_colon():
    " Tests that create_time contains a colon"
    assert ":" in create_time("1111")


def test_create_time_1():
    " Tests that create time makes the correct time string"
    assert create_time("2359") == "23:59"


def test_create_time_2():
    " Tests that create time makes the correct time string"
    assert create_time("0000") == "00:00"


# Tests that all_combos_of_four makes all combinations of numbers given four starting numbers


def test_all_combos_of_four_length():
    " Tests that there are 24 entries in the list when all digits different"
    assert len(all_combs_of_four("1234")) == 24


def test_all_combos_of_four_duplicates():
    " Tests that there are 24 entries in the list when some digits dplicates"
    assert len(all_combs_of_four("1123")) == 24


def test_all_combos_of_four_all_same():
    " Tests that there are 24 entries when all digits same"
    assert len(all_combs_of_four("1111")) == 24


def test_all_combos_of_four_each_length_4():
    " Tests that all 24 entries are length 4"
    # Arrange
    combos = all_combs_of_four("1234")
    # Act
    for combo in combos:
        # Assert
        assert len(combo) == 4


def test_all_combos_of_four_contain_original_digits():
    " Tests all numbers have one of each of the input digits"
    # Arrange
    combos = all_combs_of_four("1234")
    # Act
    for combo in combos:
        for digit in combo:
            # Assert
            assert digit in "1234"


def test_all_combos_of_four__contains_original():
    " Tests that the original string is included as a combination"

    combos = all_combs_of_four("1234")

    assert "1234" in combos


def test_all_combos_of_four__contains_reverse():
    " Tests that the original string reversed is included as a combination"

    combos = all_combs_of_four("1234")

    assert "4321" in combos


# Tests that check_if_time_valid correctly identifies for digit numbers that can be times


def test_check_if_time_valid_True_1():
    "Tests if function returns True correctly for largest possible time"
    assert check_if_time_valid("2359")


def test_check_if_time_valid_True_2():
    "Tests if function returns True correctly for smallest possible time"
    assert check_if_time_valid("0000")


def test_check_if_time_valid_False_1():
    "Tests if function returns False correctly"
    assert check_if_time_valid("2400") == False


def test_check_if_time_valid_False_2():
    "Tests if function returns False correctly"
    assert check_if_time_valid("0060") == False


def test_check_if_time_valid_False_3():
    "Tests if function returns False correctly"
    assert check_if_time_valid("2460") == False


# Tests that largest_time correctly identifies for digit numbers that can be times


def test_largest_time_maximal():
    "Tests if largest_time works for largest possible time input"
    assert largest_time("2359") == "23:59"


def test_largest_time_zeros():
    "Tests if largest_time works for only zeroes"
    assert largest_time("0000") == "00:00"


def test_largest_time_arrangement_1():
    "Tests if largest_time picks largest possible arrangement"
    assert largest_time("1738") == "18:37"


def test_largest_time_arrangement_2():
    "Tests if largest_time picks largest possible arrangement"
    assert largest_time("1230") == "23:10"


def test_largest_time_arrangement_duplicates():
    "Tests if largest_time works for duplicates"
    assert largest_time("2222") == "22:22"
