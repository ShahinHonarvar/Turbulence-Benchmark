
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 56 to 57 (both inclusive)
    for i in range(56, 58):
        # Check if current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to sum
            sum += my_list[i]
    # Return sum
    return sum
