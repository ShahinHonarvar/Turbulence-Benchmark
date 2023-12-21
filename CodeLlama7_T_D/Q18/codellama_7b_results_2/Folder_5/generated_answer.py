
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the range of integers to consider
    sum = 0
    lower_bound = -6
    upper_bound = 4

    # Iterate over the list, checking each integer for divisibility by either -6 or 4
    for i in range(len(my_list)):
        if my_list[i] % lower_bound == 0 or my_list[i] % upper_bound == 0:
            # If the current integer is divisible by either -6 or 4, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -6 or 4 from index 0 to index 1, both inclusive. If no such integers exist in the specified range, return 0.
    return sum
