
import pandas as pd
from itertools import product

Error_message = "A valid time cannot be made from these four numbers."


def allowed_input(four_numbers: str) -> bool:
    "Checks if the original string is an allowed input (not an allowed time)"

    if len(four_numbers) != 4:
        return False

    nums = "0123456789"

    # Checks if each character is a whole number
    for character in four_numbers:
        if character not in nums:
            return False

    return True


def number_list(four_numbers: str) -> list[int]:
    "Converts a string of 4 numbers into a list of 4 integers"

    num_list = []

    for number in four_numbers:
        num_list.append(int(number))

    return num_list


def largest_value_from(max_val, nums: list[int]) -> int:
    "Given a list, it sorts it into descending order, and returns "
    "the largest value in it starting from a specified number"

    # Sorts the list of numbers into descending order
    descending_nums = sorted(nums, reverse=True)

    allowed_nums = []

    # Appends the number to a list if is allowed
    for number in descending_nums:
        if number <= max_val:
            allowed_nums.append(number)

    # As the numbers have already been sorted into descending order,
    # The first valid number is at the 0th index

    if allowed_nums == []:
        return "Error"

    else:
        return allowed_nums[0]


def create_time(final_nums: list[int]) -> str:

    time = ""

    time += str(final_nums[0]) + str(final_nums[1])
    time += ":"
    time += str(final_nums[2]) + str(final_nums[3])

    return time


def largest_time(four_nums: str) -> str:

    # Checking if the input string is initially valid
    if allowed_input(four_nums) == False:
        return Error_message

    # Making an empty list to append values to in order
    time_list = []

    # Making the input string into a list of four numbers
    digits_list = number_list(four_nums)

    # Obtaining the largest possible number for the first time digit
    first_digit = largest_value_from(2, digits_list)

    if first_digit == "Error":
        return Error_message
    else:
        # Adds first digit to the time list
        time_list.append(first_digit)
        # Removes first instance of this digit from the digits list to avoid double counting
        digits_list.remove(first_digit)

    # Obtaining the largest possible number for the second time digit

    if first_digit == 2:
        second_digit = largest_value_from(3, digits_list)
    else:
        second_digit = largest_value_from(9, digits_list)

    if second_digit == "Error":
        return Error_message
    else:
        # Adds second digit to the time list
        time_list.append(second_digit)
        # Removes first instance of this digit from the digits list to avoid double counting
        digits_list.remove(second_digit)

    # Obtaining the largest possible number for the third time digit
    third_digit = largest_value_from(5, digits_list)

    if third_digit == "Error":
        return Error_message
    else:
        # Adds first digit to the time list
        time_list.append(third_digit)
        # Removes first instance of this digit from the digits list to avoid double counting
        digits_list.remove(third_digit)

    # Adding the last digit to the time string
    time_list.append(digits_list[0])

    return (create_time(time_list))
