
def if_perfect_num(my_list):
    # Check if the list has at least 50 elements
    if len(my_list) < 50:
        return False

    # Find the number at index 49
    num = my_list[49]

    # Check if the number is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If it's a perfect number, return True
            return True

    # If we get here, the number is not a perfect number, so return False
    return False
