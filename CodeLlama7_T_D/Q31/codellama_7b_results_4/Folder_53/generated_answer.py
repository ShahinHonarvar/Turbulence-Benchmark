
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 73 elements
    if len(my_list) < 73:
        return False

    # Get the integer at index 73
    num = my_list[73]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i == i:
                return True

    return False
