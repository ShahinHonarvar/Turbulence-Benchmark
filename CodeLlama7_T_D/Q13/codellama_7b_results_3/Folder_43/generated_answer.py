
def find_second_largest_num(my_list):
    # Check if list is empty or has fewer than two elements
    if len(my_list) < 2:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate over the list, starting from index 68
    for i in range(68, len(my_list)):
        # If the current element is larger than the previous largest element, and not equal to the second largest element (if it exists), then update the second largest element and its index
        if my_list[i] > my_list[i - 1] and (second_largest is None or my_list[i] != second_largest):
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element and its index, or 'None' if no such element exists
    return second_largest, second_largest_index
