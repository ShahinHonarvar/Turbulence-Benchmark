
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate over the specified range of the input list
    for i in range(25, 71):

        # Check if the current integer is divisible by both 74 and 15
        if my_list[i] % 74 == 0 and my_list[i] % 15 == 0:

            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both 74 and 15 from index 25 to index 70, both inclusive
    return divisible_integers
