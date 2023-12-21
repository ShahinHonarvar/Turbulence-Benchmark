
def if_perfect_num(my_list):
    # Check if the list has at least 57 elements
    if len(my_list) < 57:
        return False

    # Get the integer at index 56
    perfect_number = my_list[56]

    # Check if the integer is a perfect number
    if perfect_number == sum(range(1,perfect_number))) :

        return True


    else:

        return False
