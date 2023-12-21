
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the integer at index 91
    num = my_list[91]

    # Check if the integer is a perfect number
    if (num > 0) and (sum(range(1, num)) == num):
        return True

    else:
        return False
