
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range and the divisors
    start = 81
    end = 86
    div_33 = -33
    div_62 = -62
    # Initialize the sum to 0
    total_sum = 0
    # Iterate through the list in the specified range
    for i in range(start, end + 1):
        # Check if the current element is divisible by either of the two divisors
        if my_list[i] % div_33 == 0 or my_list[i] % div_62 == 0:
            # If it is, add it to the total sum
            total_sum += my_list[i]
    # Return the total sum
    return total_sum
