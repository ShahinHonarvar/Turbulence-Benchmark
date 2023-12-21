
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    i = 0

    # Iterate through the list of integers
    while i < len(my_list):
        # Check if the current integer is divisible by either -1 or 13
        if my_list[i] % (-1) == 0 or my_list[i] % (13) == 0:
            # If it is, add it to the total
            total += my_list[i]

        # Increment the iterator variable
        i += 1

    # Return the sum of all integers divisible by either -1 or 13 from index 0 to index 5, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
