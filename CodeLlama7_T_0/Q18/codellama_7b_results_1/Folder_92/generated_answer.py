
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    i = 0

    # Loop through the list and calculate the sum of all integers divisible by either 1 or -1
    while i < len(my_list):
        if my_list[i] % 1 == 0 or my_list[i] % -1 == 0:
            total += my_list[i]

        i += 1

    # Return the sum of all integers divisible by either 1 or -1 from index 0 to index 0, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
