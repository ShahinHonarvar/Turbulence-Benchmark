
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the specified range of indices in the input list
    for i in range(18, 38 + 1):
        # Check if the current element is divisible by -97
        if my_list[i] % -97 == 0:
            # If it is divisible, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all divisible integers
    return div_ints
