
def if_perfect_num(my_list):
    # Check if the index is within the list range
    if len(my_list) - 1 < 126:
        return False

    # Check if the number at index 126 is a perfect number
    if my_list[126] == 0:
        return False

    for i in range(1, int(my_list[126]) / 2 + 1):
        if my_list[126] % i == 0:
            if (my_list[126] / i) == i:
                return True

    return False
