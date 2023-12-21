
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers, starting from index 14 and ending at index 93, inclusive
    for i in range(14, 93 + 1):
        # Check if the current integer is divisible by both 71 and 81
        if my_list[i] % 71 == 0 and my_list[i] % 81 == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 71 and 81 from index 14 to index 93, both inclusive
    return divisible_ints
