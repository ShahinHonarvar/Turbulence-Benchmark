
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices and the sum
    start_index = 55
    end_index = 80
    sum = 0

    # Iterate over the specified range of indices in the list
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either 22 or 32
        if my_list[i] % 22 == 0 or my_list[i] % 32 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either 22 or 32 from index 55 to index 80, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
