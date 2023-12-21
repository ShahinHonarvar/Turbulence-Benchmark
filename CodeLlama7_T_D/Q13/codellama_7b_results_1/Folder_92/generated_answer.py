
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # If the second element from index 0 to index 1, both inclusive, is not equal to the first element, then return it
    if my_list[1] != my_list[0]:
        return my_list[1]

    # Otherwise, return None
    else:
        return None
