
def all_even_ints_exclusive(my_list):
    # Get the starting and ending indices of the range
    start_index = 55
    end_index = 84
    # Create an empty list to store the even integers
    even_ints = []
    # Iterate through the list, starting from the specified index
    for i in range(start_index, end_index):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 55 to index 84, both exclusive
    return even_ints
