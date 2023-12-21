
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Find the second largest element
    for i in range(10, 100 + 1):
        if my_list[i] > my_list[i - 1]:
            return my_list[i]

    # If there is no such element, return None
    return None
