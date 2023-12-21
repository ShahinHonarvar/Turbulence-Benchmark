
def if_perfect_num(my_list):
    # Check if the list has at least 19 elements
    if len(my_list) < 19:
        return False

    # Get the number at index 18
    num = my_list[18]

    # Check if the number is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
