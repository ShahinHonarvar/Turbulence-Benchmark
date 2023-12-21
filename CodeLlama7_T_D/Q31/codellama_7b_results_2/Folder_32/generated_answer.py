
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 850 elements
    if len(my_list) < 850:
        return False

    # Find the number at index 849
    num = my_list[849]

    # Check if the number is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
