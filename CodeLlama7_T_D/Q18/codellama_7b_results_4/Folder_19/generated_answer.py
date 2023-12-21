
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 1
    end_index = 4

    # Iterate through the list and calculate the sum of integers divisible by either 4 or -6
    for i in range(start_index, end_index + 1):
        if my_list[i] % 4 == 0 or my_list[i] % -6 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 4 or -6 from index 1 to index 4, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
