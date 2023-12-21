
def if_perfect_num(my_list):
    # Check if the list has at least 21 elements
    if len(my_list) < 21:
        return False

    # Get the number at index 21
    num = my_list[21]

    # Check if the number is a perfect number
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            if (num / i) - 1 == i:
                return True

    return False
