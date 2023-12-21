
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 62 to index 92, both inclusive
    for i in range(62, 93):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add current element to sum
            sum += my_list[i]
    # Return sum
    return sum
