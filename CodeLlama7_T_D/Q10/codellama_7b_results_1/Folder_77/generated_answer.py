
def all_odd_ints_exclusive(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return []

    # Get the start and end indices of the range
    start = 111
    end = 473

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list from the start index to the end index
    for i in range(start, end):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list of odd integers
            odd_ints.append(my_list[i])

    return odd_ints
