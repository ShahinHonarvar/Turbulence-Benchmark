
def if_perfect_num(lst):
    # Check if the list has an element at index 849
    if len(lst) - 1 >= 849:
        # Get the integer at index 849
        num = lst[849]
        # Check if the integer is a perfect number
        if (num - 1) * (num + 1) / 2 == num ** 2:
            return True

    return False
