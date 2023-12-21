
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list of integers
    for i in range(len(my_list)):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add current element to sum
            sum += my_list[i]
    return sum
