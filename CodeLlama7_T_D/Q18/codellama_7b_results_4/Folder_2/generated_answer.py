 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 73
    end_index = 86
    sum = 0

    # Iterate through the list and calculate the sum of all integers divisible by either 54 or 82 from index 73 to index 86, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 54 == 0 or my_list[i] % 82 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 54 or 82 from index 73 to index 86, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
