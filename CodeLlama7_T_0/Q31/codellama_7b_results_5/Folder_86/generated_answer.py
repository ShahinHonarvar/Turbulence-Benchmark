
def if_perfect_num(my_list):
    # Check if the list has at least 195 elements
    if len(my_list) < 195:
        return False

    # Get the value of the 194th element
    num = my_list[194]

    # Check if the number is a perfect square
    root = int(num ** 0.5)
    if root ** 2 == num:
        return True

    # If the number is not a perfect square, check if it is a perfect cube
    root = int(num ** (1/3))
    if root ** 3 == num:
        return True

    # If the number is not a perfect square or cube, return False
    return False
