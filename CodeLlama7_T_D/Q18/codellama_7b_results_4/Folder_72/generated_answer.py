
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 38
    end_index = 81
    sum = 0

    # Iterate over the list and calculate the sum of all integers divisible by either -61 or -71 from index 38 to index 81, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-61) == 0 or my_list[i] % (-71) == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either -61 or -71 from index 38 to index 81, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
