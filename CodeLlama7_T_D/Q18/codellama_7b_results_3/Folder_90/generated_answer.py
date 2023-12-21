
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    num_range = range(138, 425)
    # Loop through the numbers in the specified range
    for i in num_range:
        # Check if the current number is divisible by either -863 or -329
        if my_list[i] % -863 == 0 or my_list[i] % -329 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of all integers divisible by either -863 or -329 from index 138 to index 424, both inclusive.
    return sum
