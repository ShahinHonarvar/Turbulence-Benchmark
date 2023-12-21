
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 86
    end_index = 90
    divisor1 = -71
    divisor2 = -67
    total_sum = 0

    # Check if the list is valid and has elements between the specified range
    if my_list is None or len(my_list) < end_index:
        return 0

    # Iterate through the list and add up all integers divisible by either -71 or -67 from index 86 to index 90, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor1 == 0 or my_list[i] % divisor2 == 0:
            total_sum += my_list[i]

    # Return the sum of all integers divisible by either -71 or -67 from index 86 to index 90, both inclusive
    return total_sum
