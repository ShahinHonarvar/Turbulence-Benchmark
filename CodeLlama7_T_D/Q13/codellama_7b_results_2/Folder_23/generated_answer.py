
def find_second_largest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Find the second largest element
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1]:
            continue

        elif my_list[i] < my_list[i + 1]:
            return my_list[i + 1]

    # If there is no second largest element, return None
    return None
