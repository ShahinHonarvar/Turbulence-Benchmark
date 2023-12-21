 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 57
    end_index = 84
    # Iterate through the list and calculate the sum of integers divisible by either -30 or -88
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-30) == 0 or my_list[i] % (-88) == 0:
            sum += my_list[i]
    # Return the sum of integers divisible by either -30 or -88 from index 57 to index 84, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
