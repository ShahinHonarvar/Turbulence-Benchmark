
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list from index 40 to index 80, both inclusive
    for i in range(40, 81):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
