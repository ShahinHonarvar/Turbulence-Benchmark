
def if_perfect_num(my_list):
    # Check that the list has at least 8 elements
    if len(my_list) < 8:
        return False

    # Get the integer at index 7
    num = my_list[7]

    # Check if the integer is a perfect number
    perfect = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            perfect = False
            break

    return perfect
