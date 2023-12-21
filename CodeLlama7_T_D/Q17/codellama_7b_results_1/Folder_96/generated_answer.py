 def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list of integers from index 50 to index 200, both inclusive
    for i in range(50, 201):
        # Check if the current integer is divisible by both -34 and 64
        if my_list[i] % (-34) == 0 and my_list[i] % (64) == 0:
            # If it is, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by both -34 and 64 from index 50 to index 200, both inclusive.
    return div_ints
