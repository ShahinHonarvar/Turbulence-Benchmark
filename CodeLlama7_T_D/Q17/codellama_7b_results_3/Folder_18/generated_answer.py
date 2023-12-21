
def all_ints_div_by_both_two_nums(my_list):
    # Find the index of the first element in the range
    start_index = 55

    # Find the index of the last element in the range
    end_index = 66

    # Create an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the elements in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by both 22 and 82
        if my_list[i] % 22 == 0 and my_list[i] % 82 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 22 and 82 from index 55 to index 66, both inclusive.
    return divisible_ints
