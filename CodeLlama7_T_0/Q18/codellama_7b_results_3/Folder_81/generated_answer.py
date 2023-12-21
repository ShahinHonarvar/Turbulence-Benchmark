
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 10
    end_index = 100

    # Iterate through the list and calculate the sum of all integers divisible by either 10 or 100
    for i in range(start_index, end_index + 1):
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either 10 or 100 from index 10 to index 100, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
