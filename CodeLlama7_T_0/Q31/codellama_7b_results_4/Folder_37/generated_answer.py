
def if_perfect_num(my_list):
    # Check if the list has at least 29 elements
    if len(my_list) < 29:
        return False

    # Get the integer at index 28
    num = my_list[28]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            # If the integer is a perfect number, return True
            return True

    # If the integer is not a perfect number, return False
    return False
