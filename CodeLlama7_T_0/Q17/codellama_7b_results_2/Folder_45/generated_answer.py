
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(30, 201):
        # Check if the current integer is divisible by both -115 and 115
        if my_list[i] % (-115) == 0 and my_list[i] % (115) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -115 and 115 from index 30 to index 200, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
