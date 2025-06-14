
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the integer at index 845
    perfect_num = my_list[845]

    # Check if the integer is a perfect number
    if sum(range(1, perfect_num))) == 2 * perfect_num - 1:
        return True
    else:
        return False
