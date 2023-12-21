
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list, starting from index 77 and ending at index 87 (both inclusive)
    for i in range(77, 88):

        # Check if the current element is divisible by either 23 or 57
        if my_list[i] % 23 == 0 or my_list[i] % 57 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
