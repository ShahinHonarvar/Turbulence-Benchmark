
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Loop through the specified range of the input list
    for i in range(36, 85 + 1):
        # Check if the current integer is divisible by both -27 and -96
        if my_list[i] % -27 == 0 and my_list[i] % -96 == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    return divisible_integers
