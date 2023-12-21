
def if_perfect_num(my_list):
    # Check if the list has at least 53 elements
    if len(my_list) < 53:
        return False

    # Get the integer at index 53
    perfect_number = my_list[53]

    # Check if the integer is a perfect number
    if (perfect_number - 1) / 2 * 2 == perfect_number:
        return True

    else:

        return False
