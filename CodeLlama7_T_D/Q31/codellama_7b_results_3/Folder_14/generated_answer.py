
def if_perfect_num(lst):
    # Check if the list has at least 17 elements
    if len(lst) < 17:
        return False

    # Get the integer at index 17
    num = lst[17]

    # Check if the integer is a perfect number
    if num > 0 and sum(range(1, num))) == 2*num - 1:
        return True

    else:

        return False
