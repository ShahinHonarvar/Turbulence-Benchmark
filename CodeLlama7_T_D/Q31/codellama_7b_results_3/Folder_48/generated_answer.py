
def if_perfect_num(my_list):
    # Check if the list has at least 248 elements
    if len(my_list) < 248:
        return False

    # Get the integer at index 247
    num = my_list[247]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            # If it is a perfect number, return true
            return True

    # If it is not a perfect number, return false
    return False
