
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 453 elements
    if len(my_list) < 453:
        return False

    # Get the integer at index 453
    perfect_num = my_list[453]

    # Check if the integer is a perfect number
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            return True

    return False
