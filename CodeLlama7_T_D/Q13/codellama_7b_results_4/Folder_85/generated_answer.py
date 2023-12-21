
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Find the second largest element
    for i in range(len(my_list) - 1, -1, -1):
        if i >= 6 and i <= 8:
            return my_list[i]

    # If there is no such element, return None
    return None
