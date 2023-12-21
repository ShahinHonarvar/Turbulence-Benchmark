
def all_even_ints_inclusive(my_list):
    # Define the starting and ending indices for the range of even integers
    start_idx = 55
    end_idx = 98
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list from the starting index to the ending index
    for i in range(start_idx, end_idx + 1):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from the specified range
    return even_ints
