
def find_second_largest_num(my_list):
    # Check if list is empty or None
    if not my_list:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of second largest element
    second_largest = None
    current_index = 30

    # Iterate through the list from index 30 to 48, both inclusive
    for i in range(30, 50):
        # If the current element is greater than the second largest element, update the second largest element and its index
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            current_index = i

    # Return the second largest element from index 30 to 48, both inclusive
    return second_largest
