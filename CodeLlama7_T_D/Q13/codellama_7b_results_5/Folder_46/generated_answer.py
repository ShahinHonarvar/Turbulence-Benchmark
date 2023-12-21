
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Create a copy of the list without the largest element
    remaining_elements = my_list.copy()
    remaining_elements.remove(largest)

    # Find the second largest element in the remaining elements
    second_largest = max(remaining_elements)

    # Return the second largest element if it is between indices 30 and 87, inclusive
    if second_largest >= my_list[30] and second_largest <= my_list[87]:
        return second_largest

    # Otherwise, return 'None'
    else:
        return None
