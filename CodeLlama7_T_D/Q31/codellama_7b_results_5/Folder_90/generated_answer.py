
def if_perfect_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Check if the integer at index 263 is a perfect number
    if my_list[263] % (my_list[263] - 1) == 0:
        return True

    else:

        return False
