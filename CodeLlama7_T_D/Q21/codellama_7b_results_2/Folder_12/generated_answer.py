
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the specified range of indices in the input list
    for i in range(23, 65 + 1):
        # Check if the current integer is divisible by -46
        if my_list[i] % -46 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers
    return divisible_ints
