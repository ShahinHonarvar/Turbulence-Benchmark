
def if_perfect_num(my_list):
    # Check if the list has at least 25 elements
    if len(my_list) < 25:
        return False

    # Get the integer at index 24
    num = my_list[24]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i == i:
                return True

    return False
