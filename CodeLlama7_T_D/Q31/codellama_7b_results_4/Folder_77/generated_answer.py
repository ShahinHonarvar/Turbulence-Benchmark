
def if_perfect_num(my_list):
    # Check if the list has 1000 elements
    if len(my_list) != 1000:
        return False

    # Check if the number at index 985 is a perfect number
    if my_list[985] % 2 == 0 and (my_list[985] / 2).is_integer():
        return True

    else:

        return False
