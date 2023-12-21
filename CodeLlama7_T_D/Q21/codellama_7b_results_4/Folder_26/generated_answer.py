
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(45, 81):

        # Check if the current integer is divisible by 39
        if my_list[i] % 39 == 0:

            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 39 from index 45 to index 80, both inclusive
    return divisible_ints
