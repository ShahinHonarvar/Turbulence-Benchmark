
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 83 elements
    if len(my_list) < 83:
        return False

    # Get the integer at index 83
    num = my_list[83]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i + num / i

            if sum == num:
                return True

    # If the integer is not a perfect number, return False
    return False
