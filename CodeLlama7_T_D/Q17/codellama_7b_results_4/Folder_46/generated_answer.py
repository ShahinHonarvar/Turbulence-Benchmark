
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(11, 46 + 1):
        # Check if the current integer is divisible by both 55 and 36
        if my_list[i] % 55 == 0 and my_list[i] % 36 == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 55 and 36 from index 11 to index 46, both inclusive
    return divisible_ints
