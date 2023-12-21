
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 51
    end_index = 76

    # Iterate through the list, starting from the specified index and ending at the specified index
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either -90 or -59
        if my_list[i] % (-90) == 0 or my_list[i] % (-59) == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all integers divisible by either -90 or -59 from index 51 to index 76, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
