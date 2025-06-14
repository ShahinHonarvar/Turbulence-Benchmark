
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the specified range of the input list
    for i in range(78, 91):
        # Check if the current integer is divisible by both 76 and 60
        if my_list[i] % 76 == 0 and my_list[i] % 60 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of divisible integers
    return divisible_ints
