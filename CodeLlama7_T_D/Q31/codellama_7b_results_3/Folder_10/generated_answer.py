
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 54 elements
    if len(my_list) < 54:
        return False

    # Get the integer at index 54
    num = my_list[54]

    # Check if the number is a perfect square
    root = int(num ** 0.5)
    if root ** 2 == num:
        return True

    return False
