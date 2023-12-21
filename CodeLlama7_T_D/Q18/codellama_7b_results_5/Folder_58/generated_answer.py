
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    curr_idx = 240
    # Loop through the list from index 240 to index 901, both inclusive
    while curr_idx <= 901:
        # Check if the current element is divisible by either 546 or 709
        if my_list[curr_idx] % 546 == 0 or my_list[curr_idx] % 709 == 0:
            # If it is, add it to the sum
            sum += my_list[curr_idx]
        # Increment the current index by 1
        curr_idx += 1
    # Return the sum of all integers divisible by either 546 or 709 from index 240 to index 901, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
