
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the function
    sum = 0
    start_index = 48
    end_index = 59
    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 88 or 58
        if my_list[i] % 88 == 0 or my_list[i] % 58 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of all integers divisible by either 88 or 58 from index 48 to index 59, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
