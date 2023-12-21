
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the specified range of the input list
    for i in range(52, 54):

        # Check if the current element is divisible by 93
        if my_list[i] % 93 == 0:

            # If so, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all divisible integers in the specified range
    return div_ints
