
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list starting from index 34
    for i in range(34, len(my_list)):

        # Check if the current element is divisible by either 27 or 57
        if my_list[i] % 27 == 0 or my_list[i] % 57 == 0:

            # If it is, add it to the total
            total += my_list[i]

    # Return the sum
    return total
