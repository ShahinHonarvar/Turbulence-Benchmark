
def if_perfect_num(my_list):
    # Check if the list has at least 18 elements
    if len(my_list) < 18:
        return False

    # Get the integer at index 17
    perfect_number = my_list[17]

    # Check if the integer is a perfect number
    if (perfect_number % 2 == 0) and sum(range(1, perfect_number // 2 + 1)) == perfect_number:
        return True

    else:

        return False
