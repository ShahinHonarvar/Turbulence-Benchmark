
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(57, 85 + 1):
        # Check if the current element is divisible by both -30 and -88
        if my_list[i] % (-30) == 0 and my_list[i] % (-88) == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -30 and -88 from index 57 to index 84, both inclusive
    return divisible_ints
