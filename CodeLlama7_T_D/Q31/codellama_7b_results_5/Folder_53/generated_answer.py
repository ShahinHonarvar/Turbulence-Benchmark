
def if_perfect_num(my_list):
    # Check if the list has enough elements
    if len(my_list) < 73:
        return False

    # Get the value at index 73
    perfect_number = my_list[73]

    # Check if the number is a perfect number
    if perfect_number > 0 and sum(range(1, perfect_number)) == perfect_number:
        return True

    else:

        return False
