
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of the input list
    for i in range(43, 60):
        # Check if the current element is divisible by 22
        if my_list[i] % 22 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 22 from index 43 to index 59, both inclusive.
    return divisible_ints
