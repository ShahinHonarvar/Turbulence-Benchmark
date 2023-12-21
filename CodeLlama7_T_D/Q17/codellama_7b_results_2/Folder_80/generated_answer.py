
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list and check if each integer is divisible by both 71 and 81
    for i in range(14, 93 + 1):
        if my_list[i] % 71 == 0 and my_list[i] % 81 == 0:
            # If the integer is divisible by both 71 and 81, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    return divisible_ints
