
def find_second_smallest_num(my_list):
    # Check if list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Get the second smallest element from index 23 to index 23, both inclusive
    try:
        second_smallest = my_list[23]
    except IndexError:
        return None

    return second_smallest
