
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list of integers from index 0 to index 7, both inclusive
    for i in range(8):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is an odd integer, add it to the sum
            sum += my_list[i]
    # Return the sum of all odd integers from index 0 to index 7, both inclusive
    return sum
