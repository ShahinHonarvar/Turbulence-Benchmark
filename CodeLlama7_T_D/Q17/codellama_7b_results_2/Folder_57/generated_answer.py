
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in my_list
    for i in range(51, 76 + 1):

        # Check if the current integer at index 'i' is divisible by both -90 and -59
        if (my_list[i] % -90 == 0) and (my_list[i] % -59 == 0)):
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -90 and -59 from index 51 to index 76, both inclusive.
    return divisible_ints
