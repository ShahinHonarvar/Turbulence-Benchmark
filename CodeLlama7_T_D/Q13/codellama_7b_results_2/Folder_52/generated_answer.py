
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Find the second largest element
    for i in range(28, 39):
        if my_list[i] > my_list[i - 1]:
            return my_list[i]

    # If no such element exists, return None
    return None
