
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers

    for i in range(421, 489 + 1):
        # Check if the current integer is divisible by 885

        if my_list[i] % 885 == 0:
            # If it is divisible, append it to the list of divisible integers

            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers

    return divisible_ints
