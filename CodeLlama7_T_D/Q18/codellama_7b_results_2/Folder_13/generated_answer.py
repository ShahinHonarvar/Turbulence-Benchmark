
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 13
    end_index = 18
    # Loop through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 45 or 20
        if my_list[i] % 45 == 0 or my_list[i] % 20 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of all integers divisible by either 45 or 20 from index 13 to index 18, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
