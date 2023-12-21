
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(7, 10):
        # Check if the current integer is divisible by both -9 and -7
        if my_list[i] % (-9) == 0 and my_list[i] % (-7) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -9 and -7 from index 7 to index 9, both inclusive
    return divisible_ints
