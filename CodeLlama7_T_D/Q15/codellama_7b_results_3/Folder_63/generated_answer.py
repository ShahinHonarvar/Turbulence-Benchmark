
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list of integers from index 22 to index 88, both inclusive
    for i in range(22, 89):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to sum
            sum += my_list[i]
    # Return sum
    return sum
