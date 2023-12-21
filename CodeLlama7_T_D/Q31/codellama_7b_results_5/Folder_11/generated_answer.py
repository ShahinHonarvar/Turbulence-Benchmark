
def if_perfect_num(my_list):
    # Check if the list has at least 78 elements
    if len(my_list) < 78:
        return False

    # Get the integer at index 77
    num = my_list[77]

    # Check if the integer is a perfect number
    if all(num % i == 0 for i in range(1, int(num ** 0.5) + 1)):
        return True

    else:

        return False
