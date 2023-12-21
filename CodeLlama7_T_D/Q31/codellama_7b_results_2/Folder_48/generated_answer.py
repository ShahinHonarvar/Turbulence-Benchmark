
def if_perfect_num(my_list):
    # Check if the list has at least 248 elements
    if len(my_list) < 248:
        return False

    # Get the element at index 247
    num = my_list[247]

    # Check if the number is a perfect number
    if all(num % i == 0 for i in range(1, int(num ** 0.5) + 1)):
        return True

    else:

        return False
