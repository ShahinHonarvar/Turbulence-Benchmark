
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    n = len(my_list)

    # Check if the index is valid
    if 13 <= n and n <= 68:
        # Sort the list in ascending order
        my_list.sort()

        # Return the second smallest element
        return my_list[12]

    else:

        # Return None if the index is invalid
        return None
