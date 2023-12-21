
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the specified range of the input list
    for i in range(29, 54):

        # Check if the current integer is divisible by both -68 and -85
        if my_list[i] % (-68) == 0 and my_list[i] % (-85) == 0:

            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both -68 and -85 from index 29 to index 53, both inclusive
    return divisible_integers
