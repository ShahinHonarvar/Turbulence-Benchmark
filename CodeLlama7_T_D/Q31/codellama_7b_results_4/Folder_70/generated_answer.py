
def if_perfect_num(my_list):
    # Check if the list has at least 846 elements
    if len(my_list) < 846:
        return False

    # Get the number at index 845
    num = my_list[845]

    # Check if the number is a perfect number
    if sum(range(1, num)) == num**2 - 1:
        return True

    else:

        return False
