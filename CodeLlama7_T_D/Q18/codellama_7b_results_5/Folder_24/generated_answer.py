
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 29

    # Loop through the list, starting from index 29
    while i < len(my_list):

        # Check if the current element is divisible by either -68 or -85
        if my_list[i] % -68 == 0 or my_list[i] % -85 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

        # Increment the current index by 1
        i += 1

    # Return the sum
    return sum
