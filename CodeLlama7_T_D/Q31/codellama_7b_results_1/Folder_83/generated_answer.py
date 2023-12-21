
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the number at index 95
    num = my_list[95]

    # Check if the number is a perfect square
    perfect_square = int(num ** 0.5)

    # Check if the number is a perfect cube
    perfect_cube = int(num ** (1/3))

    # Check if the number is a perfect number
    if num == perfect_square ** 2 or num == perfect_cube ** 3:
        return True

    else:

        return False
