
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the list
    for i in range(35, 65):
        # Check if the current integer is divisible by both -30 and -95
        if my_list[i] % (-30) == 0 and my_list[i] % (-95) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -30 and -95 from index 35 to index 64, both inclusive
    return divisible_ints
