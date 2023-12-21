
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(14, len(my_list)):
        # Check if the current integer is divisible by 18
        if my_list[i] % 18 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 18 from index 14 to index 68, both inclusive
    return divisible_ints
