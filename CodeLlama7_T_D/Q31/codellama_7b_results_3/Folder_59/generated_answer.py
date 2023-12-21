
def if_perfect_num(my_list):
    # Check if the list has three elements
    if len(my_list) != 3:
        return False

    # Check if the third element is an integer
    try:
        int(my_list[2])
    except ValueError:
        return False

    # Check if the third element is a perfect number
    if my_list[2] == 0 or my_list[2] % 10 == 0:
        return False

    divisor = 1

    while divisor * divisor <= my_list[2]:
        if my_list[2] % (divisor + 1) == 0:
            return False

        divisor += 1

    return True
