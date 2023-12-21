
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 87 elements
    if len(my_list) < 87:
        return False

    # Check if the 87th element is a perfect number

    elif is_perfect_num(my_list[87]):
        return True

    else:

        return False
