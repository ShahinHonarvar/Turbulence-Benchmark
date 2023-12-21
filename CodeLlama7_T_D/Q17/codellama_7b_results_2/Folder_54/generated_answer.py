
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(13, 92):
        # Check if the current element is divisible by both -65 and -62
        if my_list[i] % (-65 * -62) == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -65 and -62 from index 13 to index 91, both inclusive
    return divisible_ints
