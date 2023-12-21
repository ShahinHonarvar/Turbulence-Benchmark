
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the specified range of indices in the input list
    for i in range(5, 7):

        # Check if the current integer is divisible by -6
        if my_list[i] % -6 == 0:

            # If it is, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of divisible integers
    return div_ints
