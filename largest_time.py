Error_message = "A valid time cannot be made from these four numbers."


def create_time(final_nums: str) -> str:
    "Creates a string formatted to look like a time given an input string"

    time = ""

    time += final_nums[0] + final_nums[1]
    time += ":"
    time += final_nums[2] + final_nums[3]

    return time


def all_combs_of_four(four_digits: str) -> list[str]:
    "Creates all 24 combinations that can be made given four numbers"

    combos = []

    for i in range(4):
        for j in range(4):
            # Ensures an index isn't repeated
            if j != i:
                for k in range(4):
                    if k != i and k != j:
                        for l in range(4):
                            if l != i and l != j and l != k:
                                perm = four_digits[i] + four_digits[j] + \
                                    four_digits[k] + four_digits[l]
                                combos.append(perm)

    return combos


def check_if_time_valid(four_digits: list[int]) -> bool:
    "Checks if a possible time can be made given four numbers"

    # Creates the hour from the first and second digit
    hour = (int(four_digits[0]) * 10) + int(four_digits[1])

    # Creates the minute from the third and fourth digit
    minutes = (int(four_digits[2]) * 10) + int(four_digits[3])

    # Condition for a time to be valid
    if hour < 24 and minutes < 60:
        return True
    else:
        return False


def largest_time(four_nums: str) -> str:
    "Determines the largest time possible given a string of four numbers"

    combinations = all_combs_of_four(four_nums)

    # Makes a list of all possible times that can be created
    valid_times_list = []

    for number_string in combinations:
        if check_if_time_valid(number_string) == True:
            valid_times_list.append(number_string)

    if valid_times_list == []:
        return Error_message

    # Makes a copy of the list in descending order
    descending_nums = sorted(valid_times_list, reverse=True)

    largest_value = descending_nums[0]

    return create_time(largest_value)


def generate_all_input_combinations():
    "Creates a list of all positive 4 digit numbers as a strings"

    combinations = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    combinations.append(f"{i}{j}{k}{l}")
    return combinations


if __name__ == "__main__":
    combinations = generate_all_input_combinations()

    # Counts how many times an invalid time is made
    invalid_count = 0

    # creates a file called every_largest_time.csv, which automatically closes when done
    with open("every_largest_time.csv", "w") as file:

        # Header row
        file.write("Input string, Largest Time \n")

        for combo in combinations:
            result = largest_time(combo)
            file.write(f"{combo},{result}\n")

            if result == Error_message:
                invalid_count += 1

    print("Done! Check every_largest_time.csv")
    print(f"Number of valid times: {invalid_count}")
    print(f"Number of invalid times: {10000 - invalid_count}")
