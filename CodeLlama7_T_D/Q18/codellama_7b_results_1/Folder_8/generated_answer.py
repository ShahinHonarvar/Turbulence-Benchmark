
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 36
    end_index = 85
    sum = 0

    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -27 or -96
        if my_list[i] % (-27) == 0 or my_list[i] % (-96) == 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -27 or -96 from index 36 to index 85, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
