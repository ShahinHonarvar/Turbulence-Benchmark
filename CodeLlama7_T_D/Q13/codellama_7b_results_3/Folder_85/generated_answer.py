
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Get the length of the list
    list_len = len(my_list)
    # Check if the list is empty
    if list_len == 0:
        return None
    # Find the second largest element in the list
    second_largest = None
    for i in range(6, 9):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    # Return the second largest element or 'None' if no such element exists
    return second_largest
