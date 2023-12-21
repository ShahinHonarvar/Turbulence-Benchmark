
def if_perfect_num(my_list):
    # Check if the list has at least 98 elements
    if len(my_list) < 98:
        return False

    # Get the integer at index 97
    num = my_list[97]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If the integer is not a perfect number, return false
            return False

    # If the integer is a perfect number, return true
    return True
