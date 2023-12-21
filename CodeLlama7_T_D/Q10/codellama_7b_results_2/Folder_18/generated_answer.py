
def all_odd_ints_exclusive(my_list):
    # Get the length of the list
    list_len = len(my_list)
    # Set the starting and ending indices for the range
    start_index = 57
    end_index = 84
    # Check if the specified range is valid
    if start_index < 0 or start_index >= list_len:
        return []

    if end_index < 0 or end_index >= list_len:
        return []

    # Get the list of all odd integers in the specified range
    odd_ints = [my_list[i] for i in range(start_index, end_index + 1) if my_list[i] % 2 != 0]
    return odd_ints
