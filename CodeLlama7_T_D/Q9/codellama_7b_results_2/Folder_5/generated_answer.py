
def all_odd_ints_inclusive(my_list):
    # Get the starting and ending indices of the specified range
    start = 8
    end = 9
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from the starting index to the ending index
    for i in range(start, end + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list
            odd_ints.append(my_list[i])
    return odd_ints
