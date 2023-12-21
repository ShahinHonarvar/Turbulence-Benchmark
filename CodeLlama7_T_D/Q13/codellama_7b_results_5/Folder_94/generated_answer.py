
def find_second_largest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Get the indices of the second largest element
    second_largest = my_list[28:40]
    # Return the second largest element, or None if it doesn't exist
    try:
        return max(second_largest)
    except ValueError:
        return None
