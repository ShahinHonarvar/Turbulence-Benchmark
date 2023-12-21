
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 58 elements
    if len(my_list) < 58:
        return False

    # Get the integer at index 57

    perfect_num = my_list[57]

    # Check if the integer is a perfect number

    if perfect_num > 0 and sum(range(1, perfect_num + 1)) == perfect_num * (perfect_num + 1) // 2:
        return True

    else:

        return False
