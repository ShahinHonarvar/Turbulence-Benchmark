
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list from index 281 to index 694, both inclusive
    for i in range(281, 695):

        # Check if the current element is divisible by either -722 or -731
        if my_list[i] % -722 == 0 or my_list[i] % -731 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
