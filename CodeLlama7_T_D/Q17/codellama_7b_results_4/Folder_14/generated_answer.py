
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of the input list
    for i in range(7, 10):
        # Check if the current integer is divisible by both 2 and 3
        if my_list[i] % 2 == 0 and my_list[i] % 3 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of divisible integers
    return divisible_ints
