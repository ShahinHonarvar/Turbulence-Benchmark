
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    starting_index = 68
    ending_index = 99

    # Iterate through the list and calculate the sum of integers divisible by either -37 or -26
    for i in range(starting_index, ending_index + 1):
        if my_list[i] % (-37) == 0 or my_list[i] % (-26) == 0:
            sum += my_list[i]

    # Return the sum of integers divisible by either -37 or -26 from index 68 to index 99, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
