
def all_odd_ints_inclusive(my_list):
    # Define the range of indices for the search
    start = 43
    end = 51
    # Initialize an empty list to store the results
    results = []

    # Iterate over the specified range of indices in the input list
    for i in range(start, end + 1):
        # If the current element is odd, add it to the results list
        if my_list[i] % 2 != 0:
            results.append(my_list[i])

    # Return the results list
    return results
