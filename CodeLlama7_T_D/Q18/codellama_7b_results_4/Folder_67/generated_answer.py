
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 24
    end_index = 32
    # Iterate through the list from the starting index to the ending index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 35 or 87
        if my_list[i] % 35 == 0 or my_list[i] % 87 == 0:
            # If it is, add it to the total
            total += my_list[i]
    # Return the total sum of all integers divisible by either 35 or 87 from index 24 to index 32, both inclusive. If no such integers exist in the specified range, return 0.
    return total
