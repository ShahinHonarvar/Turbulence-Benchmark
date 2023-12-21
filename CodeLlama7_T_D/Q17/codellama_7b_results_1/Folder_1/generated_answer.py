
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the list
    for i in range(10, 29):

        # Check if the current integer is divisible by both -61 and -64
        if my_list[i] % (-61 * -64) == 0:

            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -61 and -64 from index 10 to index 28, both inclusive
    return divisible_ints
