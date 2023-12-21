
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if not my_list:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Check if there is a second largest element from index 64 to index 66, both inclusive
    for i in range(64, 67):
        if my_list[i] == my_list[i+1]:
            return my_list[i]

    # If there is no such element, return None
    return None
