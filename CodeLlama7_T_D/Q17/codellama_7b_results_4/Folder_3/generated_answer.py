
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(38, 52 + 1):

        # Check if the current integer is divisible by both -41 and -47
        if my_list[i] % (-41) == 0 and my_list[i] % (-47) == 0:

            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of divisible integers
    return divisible_ints
