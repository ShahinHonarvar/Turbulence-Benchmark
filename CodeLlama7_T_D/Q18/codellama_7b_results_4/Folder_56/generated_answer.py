
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for i in range(7, 10):
        # Check if the current integer is divisible by either -9 or -7
        if my_list[i] % -9 == 0 or my_list[i] % -7 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all integers divisible by either -9 or -7 from index 7 to index 9, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
