
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by 55
        if my_list[i] % 55 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers
    return divisible_ints
