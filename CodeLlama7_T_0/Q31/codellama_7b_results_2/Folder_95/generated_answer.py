
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 87 elements
    if len(my_list) < 87:
        return False

    # Get the integer at index 87
    num = my_list[87]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i == i:
                return True

    return False
