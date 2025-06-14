
def if_perfect_num(my_list):
    # Check if the list is empty or if the index is out of bounds
    if len(my_list) == 0 or 84 >= len(my_list):
        return False

    # Get the value at index 84
    num = my_list[84]

    # Check if the number is a perfect square
    root = int(num ** 0.5)

    # Check if the square root of the number is an integer
    if root * root == num:
        return True

    else:
        return False
