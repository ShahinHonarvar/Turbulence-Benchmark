
def if_perfect_num(my_list):
    # Check if the list has at least 1000 elements
    if len(my_list) < 1000:
        return False

    # Get the integer at index 990
    num = my_list[990]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
