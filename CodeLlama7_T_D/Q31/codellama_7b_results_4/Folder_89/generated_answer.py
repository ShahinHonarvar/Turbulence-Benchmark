
def if_perfect_num(lst):
    # Check if the list has at least 19 elements
    if len(lst) < 19:
        return False

    # Get the value of the 18th element in the list
    num = lst[18]

    # Check if the number is a perfect square

    root = int(num ** 0.5)

    if root ** 2 == num:
        return True

    else:
        return False
