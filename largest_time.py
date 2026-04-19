Error_message = "A valid time cannot be made from these four numbers."


def create_time(final_nums: str) -> str:

    time = ""

    time += final_nums[0] + final_nums[1]
    time += ":"
    time += final_nums[2] + final_nums[3]

    return time


def all_combs_of_four(four_digits: str) -> list[str]:

    combos = []

    for i in range(4):
        for j in range(4):
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
    hour = int((four_digits[0] * 10) + four_digits[1])
    minutes = int((four_digits[2] * 10) + four_digits[3])

    if hour < 24 and minutes < 60:
        return True
    else:
        return False


def largest_time(four_nums: str) -> str:

    # Creates a list of string combinations given 4 numbers
    combinations = all_combs_of_four(four_nums)

    valid_times_list = []

    for number_string in combinations:
        if check_if_time_valid(number_string) == True:
            valid_times_list.append(number_string)

    descending_nums = sorted(valid_times_list, reverse=True)

    return valid_times_list


def generate__all_combinations():
    combinations = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    combinations.append(f"{i}{j}{k}{l}")
    return combinations
