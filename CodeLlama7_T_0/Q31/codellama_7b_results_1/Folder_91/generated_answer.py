
def if_perfect_num(my_list):
    # Check if the list has at least 7 elements
    if len(my_list) < 7:
        return False

    # Get the integer at index 6
    num = my_list[6]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
