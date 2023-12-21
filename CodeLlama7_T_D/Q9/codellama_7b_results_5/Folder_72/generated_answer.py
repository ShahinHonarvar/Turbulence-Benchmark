
def all_odd_ints_inclusive(my_list):
    # Define a range of indices for the search
    start = 29
    end = 51
    # Create an empty list to store the results
    results = []

    # Iterate over the range of indices
    for i in range(start, end+1):
        # Check if the current index corresponds to an odd integer
        if my_list[i] % 2 != 0:
            # If it does, add it to the list of results
            results.append(my_list[i])

    # Return the list of results
    return results
