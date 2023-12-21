
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate over the list from index 42 to 43 (both inclusive)
    for i in range(42, 44):

        # Check if the current element is divisible by either 15 or 87
        if my_list[i] % 15 == 0 or my_list[i] % 87 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either 15 or 87 from index 42 to index 43 (both inclusive)
    return sum
