
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    i = 58
    j = 81

    # Iterate through the list from index 58 to 81 (inclusive)
    while i <= j:
        # Check if the current element is divisible by either 55 or 10
        if my_list[i] % 55 == 0 or my_list[i] % 10 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

        # Increment the iterator variable
        i += 1

    # Return the sum
    return sum
