
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) <= 1:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = None

    # Iterate through the list from index 40 to index 80 (inclusive)
    for i in range(40, 81):
        # If the current element is larger than the previous largest element, make it the new largest element
        if my_list[i] > my_list[-2]:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element and its index (or None if there is no such element)
    return second_largest, second_largest_index
