
def all_odd_ints_inclusive(my_list):
    # Get the length of the list
    list_len = len(my_list)
    # Check if the specified range exists
    if 82 <= list_len and 86 >= list_len:
        # Initialize an empty list to store the odd integers
        odd_ints = []
        # Iterate through the list from index 82 to index 86
        for i in range(82, 87):
            # Check if the current element is an odd integer
            if my_list[i] % 2 != 0:
                # Add the odd integer to the list
                odd_ints.append(my_list[i])
        # Return the list of all odd integers from index 82 to index 86, both inclusive
        return odd_ints
    else:
        # If the specified range does not exist, return an empty list
        return []
