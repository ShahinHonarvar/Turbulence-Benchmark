
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices
    for i in range(48, 76 + 1):

        # Check if the current integer is divisible by both -46 and -82
        if my_list[i] % (-46) == 0 and my_list[i] % (-82) == 0:

            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of divisible integers, or an empty list if no such integers exist in the specified range
    return divisible_ints
