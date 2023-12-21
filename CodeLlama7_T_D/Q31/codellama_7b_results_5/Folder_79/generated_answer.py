
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 64 elements
    if len(my_list) < 64:
        return False

    # Get the element at index 63

    num = my_list[63]

    # Check if the number is a perfect square

    root = int(num ** 0.5)

    if root ** 2 == num:
        return True

    else:
        return False
