
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 24
    end_index = 32
    # Iterate through the list and check if each integer is divisible by either 35 or 87
    for i in range(start_index, end_index + 1):
        if my_list[i] % 35 == 0 or my_list[i] % 87 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 35 or 87 from index 24 to index 32, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
