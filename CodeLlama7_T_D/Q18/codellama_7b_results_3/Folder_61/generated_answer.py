
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    # Iterate through the list and calculate the sum of all integers divisible by either -5 or -6
    for i in range(len(my_list)):
        if my_list[i] % (-5) == 0 or my_list[i] % (-6) == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either -5 or -6 from index 0 to index 6, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
