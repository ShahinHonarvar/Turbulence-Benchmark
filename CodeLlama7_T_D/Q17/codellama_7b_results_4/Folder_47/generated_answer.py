
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the list
    for i in range(42, 87 + 1):

        # Check if the current integer is divisible by both -90 and -74
        if my_list[i] % (-90) == 0 and my_list[i] % (-74) == 0:

            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -90 and -74 from index 42 to index 87, both inclusive
    return divisible_ints
