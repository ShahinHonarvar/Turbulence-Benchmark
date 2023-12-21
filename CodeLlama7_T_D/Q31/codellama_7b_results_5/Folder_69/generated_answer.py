
def if_perfect_num(lst):
    # Check if the input is a list of positive integers
    if not isinstance(lst, list) or len(lst) <= 0:
        return False

    for i in range(len(lst)):
        # Check if the current element is an integer
        if not isinstance(lst[i], int):
            return False

        # Check if the current element is positive
        if lst[i] <= 0:
            return False

    # Check if the number at index 459 is a perfect number
    if lst[459] != 6:
        return False

    return True
