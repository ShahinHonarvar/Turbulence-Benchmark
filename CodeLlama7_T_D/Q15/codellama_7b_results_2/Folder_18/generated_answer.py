
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 35 to 49 (both inclusive)
    for i in range(35, 50):
        # Check if current element is odd
        if my_list[i] % 2 != 0:
            # If it is, add it to sum
            sum += my_list[i]
    # Return sum
    return sum
