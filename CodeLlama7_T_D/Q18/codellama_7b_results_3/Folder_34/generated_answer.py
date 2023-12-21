
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers, starting from index 60 and ending at index 200 (inclusive)
    for i in range(60, 201):

        # Check if the current integer is divisible by either 9 or 11
        if my_list[i] % 9 == 0 or my_list[i] % 11 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum of all integers divisible by either 9 or 11 from index 60 to index 200 (inclusive), or 0 if no such integers exist in the specified range.
    return total
