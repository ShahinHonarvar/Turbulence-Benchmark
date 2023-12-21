
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(574, 744 + 1):
        # Check if the current element is divisible by 649
        if my_list[i] % 649 == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers from the specified range, or an empty list if no such integers exist
    return divisible_ints
