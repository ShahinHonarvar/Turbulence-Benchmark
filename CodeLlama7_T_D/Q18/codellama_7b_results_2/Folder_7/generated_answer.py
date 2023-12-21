
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 543
    end_index = 584
    sum = 0

    # Loop through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -553 or -737
        if my_list[i] % -553 == 0 or my_list[i] % -737 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -553 or -737 from index 543 to index 584, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
