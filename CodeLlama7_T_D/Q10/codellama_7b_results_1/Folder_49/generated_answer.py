
def all_odd_ints_exclusive(my_list):
    # Check if list is empty or None
    if not my_list:
        return []

    # Get length of list
    list_len = len(my_list)

    # Set starting and ending indices for odd integers
    start_idx = 80
    end_idx = 200

    # Check if there are any odd integers in the specified range
    if not any(my_list[start_idx:end_idx] % 2):
        return []

    # Return list of all odd integers from specified range
    return [x for x in my_list[start_idx:end_idx] if x % 2]
