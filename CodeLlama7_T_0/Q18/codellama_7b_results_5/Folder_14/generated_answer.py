
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 7
    end_index = 9

    # Iterate through the list and calculate the sum of all integers divisible by either 2 or 3 from index 7 to index 9, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 2 or 3 from index 7 to index 9, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
