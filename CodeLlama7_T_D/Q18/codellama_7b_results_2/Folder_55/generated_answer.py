
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the range of indices
    sum = 0
    for i in range(10):
        # Check if the current index is divisible by either 10 or 100
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
