
def all_even_ints_inclusive(my_list):
    # Get the range of indices for the specified list
    start_index = 27
    end_index = 55
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate over the range of indices for the specified list
    for i in range(start_index, end_index + 1):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # Add the current element to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 27 to index 55, both inclusive
    return even_ints
