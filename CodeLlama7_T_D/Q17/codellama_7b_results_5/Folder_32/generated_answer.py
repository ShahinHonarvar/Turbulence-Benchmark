
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Loop through the specified range of indices in the input list
    for i in range(25, 96):
        # Check if the current integer is divisible by both 51 and 77
        if my_list[i] % 51 == 0 and my_list[i] % 77 == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    return divisible_integers
