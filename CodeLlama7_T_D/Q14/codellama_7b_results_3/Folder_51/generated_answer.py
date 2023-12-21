
def find_second_smallest_num(my_list):
    # Check if list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Return the second smallest element from index 1 to index 8, both inclusive
    for i in range(1, 9):
        if my_list[i] != my_list[i - 1]:
            return my_list[i]

    # If there is no such an element, return None
    return None
