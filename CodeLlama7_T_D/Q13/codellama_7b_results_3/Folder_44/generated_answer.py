
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Initialize variables for the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 13 to index 68, both inclusive
    if second_largest_index >= 13 and second_largest_index <= 68:
        return second_largest

    # If there is no such element, return 'None'
    else:
        return None
