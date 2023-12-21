
def if_perfect_num(my_list):
    # Check if the list has enough elements
    if len(my_list) < 17:
        return False

    # Get the integer at index 17
    num = my_list[17]

    # Check if the integer is a perfect number
    if (num - 1) * (num + 1) / 2 == num ** 2:
        return True

    else:

        return False
