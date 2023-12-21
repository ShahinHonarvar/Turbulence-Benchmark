
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 276 is a perfect number
    if my_list[276] == 1 or my_list[276] % (my_list[276] - 1) != 0:
        return False

    # If we reach this point, the element at index 276 is a perfect number
    return True
