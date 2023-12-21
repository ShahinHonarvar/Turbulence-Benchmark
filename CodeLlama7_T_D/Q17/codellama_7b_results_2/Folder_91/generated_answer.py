
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by both 8 and -3
        if my_list[i] % 8 == 0 and my_list[i] % (-3) == 0:
            # If it is, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of divisible integers
    return divisible_ints
