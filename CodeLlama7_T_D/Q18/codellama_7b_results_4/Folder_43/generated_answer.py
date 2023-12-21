
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices and the sum
    start_index = 57
    end_index = 85
    sum = 0

    # Iterate through the list within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -77 or -32
        if my_list[i] % (-77) == 0 or my_list[i] % (-32) == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -77 or -32 from index 57 to index 85, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
