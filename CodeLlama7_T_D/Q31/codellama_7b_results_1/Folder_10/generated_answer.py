
def if_perfect_num(my_list):
    # Check if the list has at least 55 elements
    if len(my_list) < 55:
        return False

    # Get the value at index 54
    perfect_number = my_list[54]

    # Check if the number is a perfect square
    root = int(perfect_number ** 0.5)
    if root ** 2 == perfect_number:
        return True

    else:

        return False
