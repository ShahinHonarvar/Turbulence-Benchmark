
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(315, 934 + 1):
        # Check if the current element is divisible by both -897 and -556
        if my_list[i] % (-897 * -556) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -897 and -556 from index 315 to index 934, both inclusive
    return divisible_ints
