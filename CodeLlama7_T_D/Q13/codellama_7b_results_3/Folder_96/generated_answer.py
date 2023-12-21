
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the index of the largest element in the list
    largest_idx = my_list.index(max(my_list))

    # If the largest element is not at index 15 to index 51, inclusive, return 'None'
    if largest_idx < 15 or largest_idx > 51:
        return None

    # Find the second largest element in the list
    second_largest = max(my_list[:largest_idx] + my_list[largest_idx+1:])

    # Return the second largest element
    return second_largest
