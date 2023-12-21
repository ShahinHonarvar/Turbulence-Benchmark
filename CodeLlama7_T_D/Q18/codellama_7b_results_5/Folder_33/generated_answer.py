
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 281
    end_index = 694
    # Iterate through the list and calculate the sum of integers divisible by either -722 or -731 from index 281 to index 694, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % -722 == 0 or my_list[i] % -731 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either -722 or -731 from index 281 to index 694, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
