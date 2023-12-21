
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in my_list
    for i in range(32, 100 + 1):

        # Check if the current integer is divisible by both -11 and -15
        if my_list[i] % (-11 * -15) == 0:

            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -11 and -15 from index 32 to index 99, both inclusive
    return divisible_ints
