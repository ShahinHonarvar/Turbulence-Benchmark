
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 86
    end_index = 89

    # Check if the list is long enough to contain the specified range
    if len(my_list) - start_index < end_index:
        return 0

    # Loop through the specified range and sum up all integers divisible by either -61 or -79
    for i in range(start_index, end_index + 1):
        if my_list[i] % -61 == 0 or my_list[i] % -79 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either -61 or -79 from index 86 to index 89, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
