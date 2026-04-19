

from largest_time import allowed_input, number_list, largest_value_from, create_time

""" Tests that validate_input correctly splits a string of 4 numbers into a list of 4 integers """


def test_validate_input_length_above_4():
    """ Tests that validate_input False if the string is 5 or more characters long """
    assert allowed_input("12345") == False
    assert allowed_input("123456789") == False


def test_validate_input_length_below_4():
    """ Tests that validate_input returns False if the string is less than 4 characters long"""
    assert allowed_input("123") == False
    assert allowed_input("") == False


""" Tests that number_list correctly splits a string of 4 numbers into a list of 4 integers """


def test_number_list_distinct_nums():
    "Tests that number_split correctly creates a list when given 4 distinct integers"
    assert number_list("1234") == [1, 2, 3, 4]
    assert number_list("9567") == [9, 5, 6, 7]


def test_number_split_distinct_nums():
    "Tests that number_split correctly creates a list when given repeated integers"
    assert number_list("1224") == [1, 2, 2, 4]
    assert number_list("9555") == [9, 5, 5, 5]


""" Tests that number_split correctly splits a string of 4 numbers into a list of 4 integers """


def test_largest_value_from():
    "Tests that largest_value_from correctly returns the first instance of a number"
    "Equal or greater to the specified max limit"
    assert largest_value_from(2, [0, 1, 2, 3]) == 2
    assert largest_value_from(3, [4, 2, 3, 1]) == 3
    assert largest_value_from(5, [5, 2, 1, 7]) == 5
    assert largest_value_from(9, [2, 9, 6, 3]) == 9


def test_largest_value_from_invalid():
    "Tests that largest_value_from returns an error string if there are no valid numbers in"
    "the desired range."
    assert largest_value_from(2, [4, 6, 7, 8]) == "Error"


""" Tests that create time correctly makes a time string from a list of four integers """


def test_create_time_length():
    " Tests that create_time makes a string 5 characters long"
    assert len(create_time([1, 1, 1, 1])) == 5


def test_create_time_colon():
    " Tests that create_time contains a colon"
    assert ":" in create_time([1, 1, 1, 1])


def test_create_time():
    " Tests that create time makes the correct time string"
    assert create_time([2, 3, 3, 5]) == "23:35"
    assert create_time([0, 0, 0, 0]) == "00:00"


""" Tests that create time correctly makes a time string from a list of four integers """
