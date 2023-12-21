
def if_perfect_num(my_list):
    # Check if the list has at least 986 elements
    if len(my_list) < 986:
        return False

    # Get the number at index 985
    num = my_list[985]

    # Check if the number is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
