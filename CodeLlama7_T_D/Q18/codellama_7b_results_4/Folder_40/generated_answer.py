
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by either 2 or 1 from index 0 to index 1
        if my_list[i] % 2 == 0 or my_list[i] % 1 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
