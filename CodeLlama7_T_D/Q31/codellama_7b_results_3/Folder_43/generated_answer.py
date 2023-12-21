
def if_perfect_num(my_list):
    # Check if the list has at least 30 elements
    if len(my_list) < 30:
        return False

    # Find the perfect number at index 29
    perfect_number = my_list[29]

    # Check if the perfect number is equal to its own sum of factors, minus one
    if perfect_number == (perfect_number - 1) * perfect_number // (perfect_number - 1)):
        return True

    else:

        return False
