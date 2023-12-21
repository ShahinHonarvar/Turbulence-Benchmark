
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers
    for i in range(len(my_list)):

        # If the current integer is divisible by either 1 or -1, add it to the total
        if my_list[i] % 1 == 0 or my_list[i] % -1 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either 1 or -1 from index 0 to index 0, both inclusive. If no such integers exist in the specified range, return 0.
    return total
