
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate over the specified range of the list
    for i in range(56, 58):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
