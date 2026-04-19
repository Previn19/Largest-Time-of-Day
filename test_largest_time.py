

from largest_time import create_time, all_combs_of_four, check_if_time_valid

""" Tests that create_time correctly makes a time string from a list of four integers """


def test_create_time_length():
    " Tests that create_time makes a string 5 characters long"
    assert len(create_time("1111")) == 5


def test_create_time_colon():
    " Tests that create_time contains a colon"
    assert ":" in create_time("1111")


def test_create_time():
    " Tests that create time makes the correct time string"
    assert create_time("2335") == "23:35"
    assert create_time("0000") == "00:00"


""" Tests that create_time correctly makes a time string from a list of four integers """


def test_all_combos_of_four_length():
    assert len(all_combs_of_four("1234")) == 24


""" Tests that check_if_time_valid correctly identifies for digit numbers that can be times"""


def test_check_if_time_valid():
    "Tests if function returns True correctly"
    assert check_if_time_valid("2359") == True
    assert check_if_time_valid("0001") == True
    assert check_if_time_valid("0000") == True


def test_check_if_time_valid():
    "Tests if function returns False correctly"
    assert check_if_time_valid("4321") == False
    assert check_if_time_valid("2400") == False
    assert check_if_time_valid("2401") == False
