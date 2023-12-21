
def if_perfect_num(my_list):
    # Check if the list has at least 927 elements
    if len(my_list) < 927:
        return False

    # Get the number at index 926
    perfect_number = my_list[926]

    # Check if the number is a perfect number
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            return True

    return False
