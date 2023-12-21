
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 22

    # Loop through the list, starting from index 22
    while i < len(my_list):
        # If the current element is divisible by either -85 or -30, add it to the sum
        if my_list[i] % (-85) == 0 or my_list[i] % (-30) == 0:
            sum += my_list[i]

        # Increment the index by 1
        i += 1

    # Return the sum of all integers divisible by either -85 or -30 from index 22 to index 24, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
