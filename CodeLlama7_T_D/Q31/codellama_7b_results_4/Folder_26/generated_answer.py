
def if_perfect_num(my_list):
    # Check if the list has at least 223 elements
    if len(my_list) < 223:
        return False

    # Get the integer at index 222
    perfect_num = my_list[222]

    # Check if the integer is a perfect number
    for i in range(1, int(perfect_num ** 0.5) + 1):
        if perfect_num % i == 0:
            # If it is a perfect number, return True
            return True

    # If it is not a perfect number, return False
    return False
