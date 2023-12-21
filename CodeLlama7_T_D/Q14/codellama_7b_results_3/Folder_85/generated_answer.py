
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Get the second smallest element from index 0 to index 6, both inclusive
    for i in range(len(my_list)):
        if i == 1:
            return my_list[i]
