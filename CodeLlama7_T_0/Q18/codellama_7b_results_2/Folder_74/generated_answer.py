
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 90
    end_index = 97

    # Iterate through the list and calculate the sum of all integers divisible by either 13 or 35 from index 90 to index 97, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 13 == 0 or my_list[i] % 35 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 13 or 35 from index 90 to index 97, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
