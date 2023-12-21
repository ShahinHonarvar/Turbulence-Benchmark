
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Loop through the list of integers from index 0 to index 9, both inclusive
    for i in range(10):

        # Check if the current integer is divisible by either 10 or 100
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
