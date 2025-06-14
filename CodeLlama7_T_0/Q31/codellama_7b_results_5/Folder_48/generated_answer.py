
def if_perfect_num(my_list):
    # Check if the list has at least 248 elements
    if len(my_list) < 248:
        return False

    # Check if the element at index 247 is a perfect number
    if my_list[247] == 0:
        return False

    for i in range(1, int(my_list[247]) ** 0.5 + 1):
        if my_list[247] % i == 0:
            j = my_list[247] / i
            if i * j == my_list[247]:
                return True

    return False
