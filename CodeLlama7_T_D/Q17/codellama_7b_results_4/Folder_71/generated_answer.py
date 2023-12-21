
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(68, 100):
        # Check if the current integer is divisible by both -37 and -26
        if my_list[i] % (-37) == 0 and my_list[i] % (-26) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -37 and -26 from index 68 to index 99, both inclusive
    return divisible_ints
