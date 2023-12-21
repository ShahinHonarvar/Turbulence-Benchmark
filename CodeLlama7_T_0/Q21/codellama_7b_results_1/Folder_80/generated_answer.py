
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(27, 86 + 1):
        # Check if the current integer is divisible by 29
        if my_list[i] % 29 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers
    return divisible_ints
