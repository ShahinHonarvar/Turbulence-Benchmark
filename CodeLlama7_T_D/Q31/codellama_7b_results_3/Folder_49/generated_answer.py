
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 68 is a perfect number
    if my_list[68] in get_perfect_numbers():
        return True

    else:

        return False
