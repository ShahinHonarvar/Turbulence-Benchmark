
def if_perfect_num(my_list):
    # Check if the list is empty
    if not my_list:
        return False

    # Get the element at index 42
    element = my_list[42]

    # Check if the element is a perfect number
    for i in range(1, int(element ** 0.5) + 1):
        if element % i == 0:
            count = 0

            while element % i == 0:
                count += 1
                element //= i

            if count > 1:
                return False

    return True
