
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the indices
    sum = 0
    i_19 = 34
    i_32 = 69
    # Iterate over the list, starting from index i_19 and ending at index i_32
    for i in range(i_19, i_32 + 1):
        # Check if the current element is divisible by either 19 or 32
        if my_list[i] % 19 == 0 or my_list[i] % 32 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of all integers divisible by either 19 or 32 from index 34 to index 69, both inclusive
    return sum
