
def if_perfect_num(my_list):
    # Check if the list is empty
    if not my_list:
        return False

    # Get the integer at index 87
    target = my_list[87]

    # Check if the integer is a perfect number
    for i in range(1, int(target ** 0.5) + 1):
        if target % i == 0:
            j = target / i
            if i * j == target:
                return True

    return False
