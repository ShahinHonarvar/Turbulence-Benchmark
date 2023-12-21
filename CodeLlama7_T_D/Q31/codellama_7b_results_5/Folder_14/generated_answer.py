
def if_perfect_num(my_list):
    # Check if the list has at least 17 elements
    if len(my_list) < 17:
        return False

    # Get the integer at index 17 of the list
    num = my_list[17]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            total = i + num / i
            if total == num:
                return True

    # If the integer is not a perfect number
    return False
