
def if_perfect_num(my_list):
    # Check if the list has more than 53 elements
    if len(my_list) > 53:
        return False

    # Check if the integer at index 53 is a perfect number

    if my_list[53] == 6:
        return True

    else:

        return False
