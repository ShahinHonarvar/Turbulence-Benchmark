
def if_perfect_num(my_list):
    # Check if the list has at least 54 elements
    if len(my_list) < 54:
        return False

    # Get the value of the 54th element in the list
    perfect_number = my_list[53]

    # Check if the perfect number is a perfect square

    if math.sqrt(perfect_number) % 1 == 0:
        return True

    else:
        return False
