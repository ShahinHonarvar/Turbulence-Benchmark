
def find_second_largest_num(my_list):
    # Check if list is empty or None
    if my_list is None or len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Get the second largest element from index 209 to index 556, both inclusive
    for i in range(209, 557):
        if my_list[i] == my_list[i - 1]:
            return my_list[i]
