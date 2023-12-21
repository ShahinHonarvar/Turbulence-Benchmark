
def all_ints_div_by_num(my_list):
    # Create a new list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in my_list
    for i in range(18, 93 + 1):
        # Check if the current integer is divisible by -85
        if my_list[i] % -85 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -85 from index 18 to index 93, both inclusive
    return divisible_ints
