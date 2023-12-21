
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers, starting from index 11 and ending at index 76 (inclusive)
    for i in range(11, 76 + 1):

        # Check if the current integer is divisible by both -81 and -94
        if my_list[i] % (-81 * -94) == 0:

            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -81 and -94 from index 11 to index 76 (inclusive)
    return divisible_ints
