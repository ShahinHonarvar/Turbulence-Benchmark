
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the integer at index 54
    perfect_number = my_list[54]

    # Check if the integer is a perfect number
    if perfect_number % (perfect_number - 1) == 0:
        return True

    else:

        return False
