
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the specified range of the input list
    for i in range(73, 82 + 1):

        # Check if the current integer is divisible by -57
        if my_list[i] % -57 == 0:

            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -57 from index 73 to index 82, both inclusive
    return divisible_ints
