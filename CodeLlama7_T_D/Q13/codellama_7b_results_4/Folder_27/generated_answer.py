 def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order

    my_list.sort()

    # Find the second largest element in the list

    for i in range(65, 94):
        if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
            return my_list[i]

    # If there is no such element, return None

    return None
