
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the specified range of the input list
    for i in range(54, 79 + 1):
        # Check if the current element is divisible by both 54 and 28
        if my_list[i] % 54 == 0 and my_list[i] % 28 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 54 and 28 from index 54 to index 79, both inclusive
    return divisible_ints
