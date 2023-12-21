
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(59, 78):

        # Check if the current integer is divisible by -95
        if my_list[i] % -95 == 0:

            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -95 from index 59 to index 77, both inclusive
    return divisible_ints
