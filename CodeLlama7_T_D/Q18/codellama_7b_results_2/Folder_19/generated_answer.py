
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list from index 1 to index 4, both inclusive
    for i in range(1, len(my_list)):
        # Check if the current element is divisible by either 4 or -6
        if my_list[i] % 4 == 0 or my_list[i] % -6 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
