
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the element at index 53
    element = my_list[53]

    # Check if the element is a perfect number
    if element == 0 or element % 2 != 0:
        return False

    sum = 0

    for i in range(1, int(element ** 0.5) + 1):
        if element % i == 0:
            sum += i

    return sum == element
