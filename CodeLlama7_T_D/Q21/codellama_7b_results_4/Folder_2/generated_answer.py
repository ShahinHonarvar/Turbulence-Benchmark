
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Loop through the specified range of indices

    for i in range(62, 71):

        # Check if the current integer is divisible by 58

        if my_list[i] % 58 == 0:

            # If it is, add it to the list of divisible integers

            div_ints.append(my_list[i])

    # Return the list of all divisible integers found in the specified range

    return div_ints
