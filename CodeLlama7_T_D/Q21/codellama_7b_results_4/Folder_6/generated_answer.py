
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Loop through the specified range of the input list
    for i in range(13, 64):

        # Check if the current element is divisible by 46
        if my_list[i] % 46 == 0:

            # If it is divisible, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all divisible integers from the specified range
    return div_ints
