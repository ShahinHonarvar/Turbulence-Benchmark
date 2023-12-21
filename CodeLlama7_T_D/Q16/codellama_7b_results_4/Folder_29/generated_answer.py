
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 59 to index 97, both inclusive
    for i in range(59, 98):
        # If current element is even
        if my_list[i] % 2 == 0:
            # Add current element to sum
            sum += my_list[i]
    # Return sum
    return sum
