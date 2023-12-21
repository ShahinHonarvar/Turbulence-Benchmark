
def if_perfect_num(my_list):
    # Check that the list has at least 850 elements
    if len(my_list) < 850:
        return False

    # Check that the element at index 849 is an integer
    try:
        my_list[849] = int(my_list[849])
    except ValueError:
        return False

    # Check if the number at index 849 is a perfect number
    if is_perfect_number(my_list[849])):
        return True

    else:

        return False
