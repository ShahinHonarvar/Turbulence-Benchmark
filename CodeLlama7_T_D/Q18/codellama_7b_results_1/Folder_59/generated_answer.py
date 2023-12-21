
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable to 0
    sum = 0

    # Iterate over the list from index 0 to index 8, both inclusive
    for i in range(len(my_list))[::-1]:

        # Check if the current element is divisible by either -3 or 8
        if my_list[i] % (-3) == 0 or my_list[i] % 8 == 0:

            # Add the current element to the sum variable
            sum += my_list[i]

    # Return the sum of all integers divisible by either -3 or 8 from index 0 to index 8, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
