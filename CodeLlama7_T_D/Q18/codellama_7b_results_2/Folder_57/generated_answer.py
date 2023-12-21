
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 51
    end_index = 76

    # Iterate through the list and calculate the sum of integers divisible by either -90 or -59
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-90 or -59) == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either -90 or -59 from index 51 to index 76, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
