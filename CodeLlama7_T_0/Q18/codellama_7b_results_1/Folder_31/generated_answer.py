
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 56
    end_index = 88
    # Iterate through the list and calculate the sum of all integers divisible by either -59 or -79 from index 56 to index 88, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % -59 == 0 or my_list[i] % -79 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either -59 or -79 from index 56 to index 88, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
