
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    len_list = len(my_list)

    # Check if the list is empty
    if len_list == 0:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(len_list):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # If the second largest element is found, return it
    if second_largest_index != -1:
        return second_largest

    # Otherwise, return None
    else:
        return None
