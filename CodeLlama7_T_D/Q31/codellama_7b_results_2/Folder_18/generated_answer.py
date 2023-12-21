
def if_perfect_num(my_list):
    # Check if the list has at least 312 elements
    if len(my_list) < 312:
        return False

    # Get the integer at index 312
    num = my_list[312]

    # Check if the integer is a perfect number
    if all(num % i == 0 for i in range(1, int(num ** 0.5) + 1)):
        return True

    else:

        return False
