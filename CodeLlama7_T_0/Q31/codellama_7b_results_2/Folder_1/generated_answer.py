
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 86 elements
    if len(my_list) < 86:
        return False

    # Get the integer at index 85
    num = my_list[85]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i == i:
                return True

    return False
