
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list from index 13 to index 18, both inclusive
    for i in range(13, 19):

        # Check if the current element is divisible by either 45 or 20
        if my_list[i] % 45 == 0 or my_list[i] % 20 == 0:

            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum
    return sum
