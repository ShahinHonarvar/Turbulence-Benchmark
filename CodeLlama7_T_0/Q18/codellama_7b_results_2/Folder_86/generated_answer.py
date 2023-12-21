
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 54
    end_index = 79

    # Iterate through the list and calculate the sum of all integers divisible by either 54 or 28 from index 54 to index 79, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 54 == 0 or my_list[i] % 28 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 54 or 28 from index 54 to index 79, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
