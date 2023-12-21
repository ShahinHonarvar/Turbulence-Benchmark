
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list from index 80 to index 200, both inclusive
    for i in range(80, 201):

        # Check if the current element is divisible by either 10 or 1000
        if my_list[i] % 10 == 0 or my_list[i] % 1000 == 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum
    return total
