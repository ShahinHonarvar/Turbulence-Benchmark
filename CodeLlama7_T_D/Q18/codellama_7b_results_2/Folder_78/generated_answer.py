
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 34 and ending at index 69 (both inclusive)
    for i in range(34, 70):
        # Check if the current element is divisible by either 19 or 32
        if my_list[i] % 19 == 0 or my_list[i] % 32 == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum
    return total
