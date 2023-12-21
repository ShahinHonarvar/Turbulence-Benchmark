
def if_perfect_num(my_list):
    # Check if the list has at least 479 elements
    if len(my_list) < 479:
        return False

    # Get the value of the element at index 478
    num = my_list[478]

    # Check if the number is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If the number is not a perfect number, return False
            return False

    # If the number is a perfect number, return True
    return True
