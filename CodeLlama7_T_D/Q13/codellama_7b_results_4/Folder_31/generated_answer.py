
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list has more than two elements
    if len(my_list) <= 2:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate over the elements of the list
    for i in range(len(my_list)):
        # If the current element is larger than the second largest element, update the second largest element and its index
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 75 to index 88, both inclusive
    if second_largest_index >= 75 and second_largest_index <= 88:
        return second_largest

    # If there is no such element, return 'None'
    else:
        return None
