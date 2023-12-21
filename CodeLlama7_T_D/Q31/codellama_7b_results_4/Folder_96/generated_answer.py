
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the number at index 47
    num = my_list[47]

    # Check if the number is a perfect number
    if num > 0 and (num - 1) % num == 0:
        return True

    else:

        return False
