
def find_second_largest_num(my_list):
    # check if the list is empty or None
    if not my_list:
        return None

    # sort the list in descending order
    my_list.sort(reverse=True)

    # iterate through the list and find the second largest element
    for i, num in enumerate(my_list):
        if i == 1:
            return num

    # if there is no such element, return None
    return None
