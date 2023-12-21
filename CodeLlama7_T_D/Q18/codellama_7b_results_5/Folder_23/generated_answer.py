
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the function
    total = 0
    start_index = 69
    end_index = 97

    # Loop through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current index is divisible by either -90 or -67
        if my_list[i] % -90 == 0 or my_list[i] % -67 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all integers divisible by either -90 or -67 from index 69 to index 97, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
