
def all_even_ints_exclusive(my_list):
    # Get the starting and ending indices of the range
    start_index = 20
    end_index = 36
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list in the specified range
    for i in range(start_index, end_index):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # Add the even integer to the list
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range
    return even_ints
