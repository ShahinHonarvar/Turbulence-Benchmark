
def all_even_ints_inclusive(my_list):
    # Find the starting and ending indices of the range
    start = 30
    end = 87
    # Create an empty list to store the even integers
    even_ints = []
    # Loop through the range of indices
    for i in range(start, end + 1):
        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:
            # If so, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range
    return even_ints
