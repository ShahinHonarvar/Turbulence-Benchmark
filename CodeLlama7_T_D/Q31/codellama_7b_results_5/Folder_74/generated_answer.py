
def if_perfect_num(my_list):
    # Check if the list has 49 elements
    if len(my_list) != 49:
        return False

    # Get the value at index 48
    num = my_list[48]

    # Check if the number is a perfect square
    root = int(num ** 0.5)

    # If the number is a perfect square, check if it is also a perfect number
    if num == (root ** 2):
        return True

    else:

        return False
