
def all_even_ints_inclusive(my_list):
    # Define the start and end indices for the range of even integers
    start_idx = 661
    end_idx = 924
    # Create an empty list to store the result
    even_ints = []
    # Iterate through the specified range of indices in the input list
    for i in range(start_idx, end_idx + 1):
        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:
            # If it does, add it to the result list
            even_ints.append(my_list[i])
    # Return the result list of even integers
    return even_ints
