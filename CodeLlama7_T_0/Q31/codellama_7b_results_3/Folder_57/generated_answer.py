
def if_perfect_num(my_list):
    # Check if the list has at least 92 elements
    if len(my_list) < 92:
        return False

    # Get the integer at index 92
    num = my_list[92]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i == i:
                return True

    return False
