
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(250, 630):
        # Check if the current element is divisible by both 850 and 587
        if my_list[i] % 850 == 0 and my_list[i] % 587 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 850 and 587 from index 250 to index 629, both inclusive
    return divisible_ints
