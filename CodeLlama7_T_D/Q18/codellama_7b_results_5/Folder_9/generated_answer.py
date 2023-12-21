
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 70
    end_index = 200
    # Iterate through the list and calculate the sum of all integers divisible by either 3 or -300 from index 70 to index 200, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % 3 == 0 or my_list[i] % -300 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 3 or -300 from index 70 to index 200, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
