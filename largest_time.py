ERROR_MESSAGE = "A valid time cannot be made from these four numbers."


def all_combs_of_four(four_digits: str) -> list[str]:
    "Creates all 24 combinations that can be made given four numbers"

    combos = []

    for i in range(4):
        for j in range(4):

            # Conditions like these ensures an index isn't repeated
            if j != i:

                for k in range(4):
                    if k not in (i, j):
                        for m in range(4):
                            if m not in (i, j, k):
                                perm = four_digits[i] + four_digits[j] + \
                                    four_digits[k] + four_digits[m]
                                combos.append(perm)

    return combos


def check_if_time_valid(four_digits: str) -> bool:
    "Checks if a possible time can be made given four numbers"

    # Creates the hour from the first and second digit
    hour = (int(four_digits[0]) * 10) + int(four_digits[1])

    # Creates the minute from the third and fourth digit
    minutes = (int(four_digits[2]) * 10) + int(four_digits[3])

    # Condition for a time to be valid
    return hour < 24 and minutes < 60


def time_to_minutes(four_digits: str) -> int:
    "Converts a four digit time string to total minutes for comparison"

    # Creates the hour from the first and second digit
    hour = (int(four_digits[0]) * 10) + int(four_digits[1])

    # Creates the minute from the third and fourth digit
    minutes = (int(four_digits[2]) * 10) + int(four_digits[3])

    return (hour * 60) + minutes


def create_time(nums: str) -> str:
    "Creates a string formatted to look like a time given an input string"
    time = nums[0] + nums[1] + ":" + nums[2] + nums[3]

    return time


def largest_time(four_nums: str) -> str:
    "Determines the largest time possible given a string of four numbers"

    combinations = all_combs_of_four(four_nums)

    # Makes a list of all possible times that can be created
    valid_times_list = []

    for number_string in combinations:
        if check_if_time_valid(number_string):
            valid_times_list.append(number_string)

    if not valid_times_list:
        return ERROR_MESSAGE

    # Obtains the time with the largest value in minutes
    largest_value = max(valid_times_list, key=time_to_minutes)

    return create_time(largest_value)


def generate_all_possible_input_combinations() -> list[str]:
    """Creates a list of all positive 4 digit numbers as a strings"""

    combinations = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for m in range(10):
                    combinations.append(f"{i}{j}{k}{m}")
    return combinations


if __name__ == "__main__":
    inputs = generate_all_possible_input_combinations()

    # Counts how many times an invalid time is made
    invalid_count = 0

    # creates a file called every_largest_time.csv, which automatically closes when done
    with open("every_largest_time.csv", "w") as file:

        # Header row
        file.write("Input string,Largest Time \n")

        for combo in inputs:
            result = largest_time(combo)
            file.write(f"{combo},{result}\n")

            if result == ERROR_MESSAGE:
                invalid_count += 1

    print("Done! Check every_largest_time.csv")
    print(f"Number of invalid times: {invalid_count}")
    print(f"Number of valid times: {len(inputs) - invalid_count}")
