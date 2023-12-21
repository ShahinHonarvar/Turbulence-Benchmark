
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the even integers in the specified range
    for i in range(23, len(my_list), 2):
        # Add the current even integer to the sum
        sum += my_list[i]
    # Return the sum
    return sum
