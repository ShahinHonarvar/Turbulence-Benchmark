
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through list from index 32 to 35, both inclusive
    for i in range(32, 36):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add current element to sum
            sum += my_list[i]
    # Return sum
    return sum
