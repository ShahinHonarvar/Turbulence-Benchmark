
def if_perfect_num(my_list):
    # Check if the list has at least 29 elements
    if len(my_list) < 29:
        return False

    # Get the value of the 28th element of the list
    perfect_number = my_list[28]

    # Check if the number is a perfect number
    for i in range(1, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            j = perfect_number / i
            if i * j == perfect_number:
                return True

    return False
