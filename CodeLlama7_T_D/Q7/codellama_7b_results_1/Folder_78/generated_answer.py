
def all_even_ints_inclusive(my_list):
    # Get the start and end indices for the specified range
    start_index = 43
    end_index = 51
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list from the start index to the end index
    for i in range(start_index, end_index + 1):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of even integers
    return even_ints
