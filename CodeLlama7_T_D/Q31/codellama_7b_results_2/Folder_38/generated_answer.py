
def if_perfect_num(my_list):
    # Check if the list has at least 39 elements
    if len(my_list) < 39:
        return False

    # Get the number at index 38
    num = my_list[38]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
