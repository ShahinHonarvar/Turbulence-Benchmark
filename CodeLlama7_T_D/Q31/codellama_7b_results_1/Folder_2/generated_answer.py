
def if_perfect_num(my_list):
    # Check if the list has at least 702 elements
    if len(my_list) < 702:
        return False

    # Get the value of the 702nd element
    num = my_list[702]

    # Check if the number is a perfect square
    sqrt_num = int(math.sqrt(num))
    if sqrt_num ** 2 == num:
        return True

    else:
        return False
