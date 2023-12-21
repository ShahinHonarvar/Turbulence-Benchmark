
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(12, 78):
        # Check if the current integer is divisible by -19
        if my_list[i] % -19 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -19 from index 12 to index 77, both inclusive.
    return divisible_ints
