
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Iterate through the specified range of indices
    for i in range(56, 89):
        # Check if the current integer is divisible by both -59 and -79
        if my_list[i] % -59 == 0 and my_list[i] % -79 == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    # Return the list of all integers divisible by both -59 and -79 from index 56 to index 88, both inclusive
    return divisible_integers
