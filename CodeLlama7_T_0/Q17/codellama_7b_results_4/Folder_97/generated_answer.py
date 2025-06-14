
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(58, 76):
        # Check if the current integer is divisible by both 72 and 62
        if my_list[i] % 72 == 0 and my_list[i] % 62 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 72 and 62 from index 58 to index 75, both inclusive
    return divisible_ints
