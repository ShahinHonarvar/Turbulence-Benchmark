
def gcf_three_nums(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Get the elements at indices 0, 8 and 3
    elem_0 = my_list[0]
    elem_8 = my_list[8]
    elem_3 = my_list[3]
    # Calculate the greatest common factor of these elements
    gcf = _gcf(elem_0, elem_8, elem_3)
    return gcf
def _gcf(a, b, c):
    # Find the minimum of a, b and c
    min_val = min(a, b, c)
    # Initialize the greatest common factor as the minimum value
    gcf = min_val
    # Loop through all the multiples of the minimum value
    for i in range(min_val, 10000000):
        # Check if i is a multiple of a, b and c
        if i % a == 0 and i % b == 0 and i % c == 0:
            # Update the greatest common factor
            gcf = i

    return gcf
