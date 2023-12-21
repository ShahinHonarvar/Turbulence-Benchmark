
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the integer at index 85
    perfect_num = my_list[85]

    # Check if the integer is a perfect number
    if (perfect_num - 1) * (perfect_num + 1) / 2 == perfect_num:
        return True

    else:

        return False
