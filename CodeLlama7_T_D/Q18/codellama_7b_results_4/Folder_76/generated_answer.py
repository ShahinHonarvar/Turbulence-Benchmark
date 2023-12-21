
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices to consider
    start_idx = 250
    end_idx = 629
    # Initialize an empty list to store the indices of integers divisible by either 850 or 587
    div_inds = []
    # Iterate over the range of indices and check if each integer is divisible by either 850 or 587
    for i in range(start_idx, end_idx + 1):
        if my_list[i] % 850 == 0 or my_list[i] % 587 == 0:
            # If the integer is divisible by either 850 or 587, add its index to the list of indices
            div_inds.append(i)
    # Initialize a variable to store the sum of all integers divisible by either 850 or 587 from index 250 to index 629
    sum = 0
    # Iterate over the list of indices and add each integer to the sum
    for i in div_inds:
        sum += my_list[i]
    # Return the sum of all integers divisible by either 850 or 587 from index 250 to index 629, both inclusive
    return sum
