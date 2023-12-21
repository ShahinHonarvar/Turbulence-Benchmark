
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the specified range of the input list
    for i in range(38, 82):
        # Check if the current integer is divisible by both -61 and -71
        if my_list[i] % (-61 * -71) == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both -61 and -71 from index 38 to index 81, both inclusive
    return divisible_integers
