
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    list_len = len(my_list)

    # Check if the list is empty
    if list_len == 0:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(list_len):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element, or None if it does not exist
    return second_largest if second_largest_index >= 70 and second_largest_index <= 84 else None
