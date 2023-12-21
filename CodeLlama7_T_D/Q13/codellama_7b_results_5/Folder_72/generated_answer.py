
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Find the second largest element
    for i in range(29, 51 + 1):
        if my_list[i] != my_list[i - 1]:
            return my_list[i]

    # If there is no such element, return None
    return None
