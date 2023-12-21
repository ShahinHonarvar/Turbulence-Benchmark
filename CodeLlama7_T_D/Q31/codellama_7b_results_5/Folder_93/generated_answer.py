
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 45 is a perfect number
    if my_list[45] in [6, 28, 496]:
        return True

    return False
