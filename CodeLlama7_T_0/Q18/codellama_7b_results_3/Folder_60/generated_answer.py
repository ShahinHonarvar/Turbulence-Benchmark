
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 10
    end_index = 79

    # Iterate through the list and calculate the sum of all integers divisible by either -74 or -58 from index 10 to index 79, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % -74 == 0 or my_list[i] % -58 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either -74 or -58 from index 10 to index 79, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
