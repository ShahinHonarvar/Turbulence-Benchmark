
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list of integers
    for i in range(len(my_list)):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # Increment sum by the current element
            sum += my_list[i]
    # Return sum
    return sum
