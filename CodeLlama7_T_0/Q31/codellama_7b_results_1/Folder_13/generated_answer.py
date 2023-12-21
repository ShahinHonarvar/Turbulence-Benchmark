
def if_perfect_num(my_list):
    # Check if the list has at least 127 elements
    if len(my_list) < 127:
        return False

    # Get the value of the 126th element in the list
    num = my_list[126]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i == i:
                return True

    return False
