
def if_perfect_num(lst):
    # Check if the list has at least 10 elements
    if len(lst) < 10:
        return False

    # Get the integer at index 10
    num = lst[10]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
