
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    total = 0
    i = 35
    while i <= 64:
        # Check if the current element is divisible by either -30 or -95
        if my_list[i] % -30 == 0 or my_list[i] % -95 == 0:
            # If it is, add it to the sum
            total += my_list[i]
        # Increment the current index by 1
        i += 1
    # Return the sum of all integers divisible by either -30 or -95 from index 35 to index 64, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
