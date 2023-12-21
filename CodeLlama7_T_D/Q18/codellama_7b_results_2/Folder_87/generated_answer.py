
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 18
    # Loop through the list, starting from index 18
    while i <= 52:
        # Check if the current element is divisible by either 15 or 57
        if my_list[i] % 15 == 0 or my_list[i] % 57 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
        # Increment the current index by 1
        i += 1
    # Return the sum of all elements divisible by either 15 or 57 from index 18 to index 52, both inclusive. If no such integers exist in the specified range, return 0.
    return sum
