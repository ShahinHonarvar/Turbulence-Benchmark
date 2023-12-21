
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(86, 91):
        # Check if the current integer is divisible by both -71 and -67
        if my_list[i] % (-71 * -67) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -71 and -67 from index 86 to index 90, both inclusive
    return divisible_ints
