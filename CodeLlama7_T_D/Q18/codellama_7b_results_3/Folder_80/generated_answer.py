
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Loop through the list of integers from index 14 to index 93, both inclusive
    for i in range(14, 94):

        # Check if the current integer is divisible by either 71 or 81
        if my_list[i] % 71 == 0 or my_list[i] % 81 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either 71 or 81 from index 14 to index 93, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
