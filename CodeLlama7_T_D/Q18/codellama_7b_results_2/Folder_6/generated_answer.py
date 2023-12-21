
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list from index 41 to index 56, both inclusive
    for i in range(41, 57):
        # Check if the current element is divisible by either 82 or 90
        if my_list[i] % 82 == 0 or my_list[i] % 90 == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum

    return total
