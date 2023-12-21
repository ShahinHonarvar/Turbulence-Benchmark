
def if_perfect_num(my_list):
    # Check if the list has at least 50 elements
    if len(my_list) < 50:
        return False

    # Check if the integer at index 49 is a perfect number
    for i in range(1, int(my_list[49]) / 2 + 1):
        if my_list[49] == sum(range(i * i, (i + 1) * (i + 1)), start=0)):
            return True

    # If the integer at index 49 is not a perfect number, return false
    return False
