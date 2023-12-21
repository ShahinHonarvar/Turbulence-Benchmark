
def if_perfect_num(my_list):
    # Check if the list has at least 50 elements
    if len(my_list) < 50:
        return False

    # Find the number at index 49
    perfect_number = my_list[49]

    # Check if the number is a perfect number
    if (perfect_number % 2 == 0) and (sum(range(1, perfect_number)) == perfect_number):
        return True

    else:

        return False
