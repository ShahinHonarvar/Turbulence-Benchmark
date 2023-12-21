
def if_perfect_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Check if the element at index 746 exists in the list
    try:
        element = my_list[746]
    except IndexError:
        return False

    # Check if the element is a perfect number
    if element == 0 or element % 2 == 0:
        return False

    for i in range(3, int(element ** 0.5) + 1, 2):
        if element % i == 0:
            return False

    return True
