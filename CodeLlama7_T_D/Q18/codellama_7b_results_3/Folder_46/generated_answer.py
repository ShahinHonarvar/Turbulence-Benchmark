
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate over the list, starting from index 11 and ending at index 46
    for i in range(11, 47):
        # Check if the current element is divisible by either 55 or 36
        if my_list[i] % 55 == 0 or my_list[i] % 36 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum

    return sum
