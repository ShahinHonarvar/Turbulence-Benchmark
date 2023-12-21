
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list of integers, starting from index 3 and ending at index 9 (inclusive)
    for i in range(3, 10):

        # Check if the current integer is divisible by either 6 or 1
        if my_list[i] % 6 == 0 or my_list[i] % 1 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum of all integers divisible by either 6 or 1 from index 3 to index 9 (inclusive), or 0 if no such integers exist in the specified range.
    return total
