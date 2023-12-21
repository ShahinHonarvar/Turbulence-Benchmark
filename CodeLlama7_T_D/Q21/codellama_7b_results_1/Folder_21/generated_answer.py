
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(572, 806 + 1):

        # Check if the current element is divisible by -158
        if my_list[i] % -158 == 0:

            # If it is, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by -158 from index 572 to index 806, both inclusive
    return div_ints
