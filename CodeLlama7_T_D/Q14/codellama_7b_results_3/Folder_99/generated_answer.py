
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Get the second smallest element from index 608 to index 609, both inclusive
    for i in range(608, 609 + 1):
        if my_list[i] != my_list[i - 1]:
            return my_list[i]

    # If there is no such an element, return None
    return None
