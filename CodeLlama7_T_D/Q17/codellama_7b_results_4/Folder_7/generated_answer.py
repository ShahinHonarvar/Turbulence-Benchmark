
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the specified range of indices in the input list
    for i in range(543, 585):
        # Check if the current integer is divisible by both -553 and -737
        if my_list[i] % (-553 * -737) == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both -553 and -737 from index 543 to index 584, both inclusive
    return divisible_integers
