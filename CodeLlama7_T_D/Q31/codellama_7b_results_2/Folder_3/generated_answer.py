
def if_perfect_num(lst):
    # Check if the list has at least 101 elements
    if len(lst) < 101:
        return False

    # Get the integer at index 100
    num = lst[100]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
