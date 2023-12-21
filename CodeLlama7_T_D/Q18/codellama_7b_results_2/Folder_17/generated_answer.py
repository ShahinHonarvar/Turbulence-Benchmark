
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate over the list from index 81 to index 89, both inclusive
    for i in range(81, 89 + 1):

        # Check if the current element is divisible by either 56 or 68
        if my_list[i] % 56 == 0 or my_list[i] % 68 == 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum of all integers divisible by either 56 or 68 from index 81 to index 89, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
