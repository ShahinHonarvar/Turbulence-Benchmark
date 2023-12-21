 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices to consider
    start_index = 315
    end_index = 934
    # Initialize an empty list to store the divisible integers
    divisible_ints = []
    # Iterate over the specified range of indices in the input list
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either -897 or -556
        if my_list[i] % (-897) == 0 or my_list[i] % (-556) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])
    # Return the sum of all divisible integers in the specified range
    return sum(divisible_ints)
