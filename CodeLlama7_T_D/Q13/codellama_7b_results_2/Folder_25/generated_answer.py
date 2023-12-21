
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if not my_list:
        return None

    # Sort the list in ascending order

    my_list.sort()

    # Get the second largest element from index 29 to index 93, both inclusive

    for i in range(29, 94):
        if my_list[i] > my_list[i - 1]:
            return my_list[i]

    # If there is no such element, return None

    return None
