
def if_perfect_num(my_list):
    # Check if the list has at least 57 elements
    if len(my_list) < 57:
        return False

    # Get the integer at index 56
    perfect_num = my_list[56]

    # Check if the integer is a perfect number
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            return True

    return False
