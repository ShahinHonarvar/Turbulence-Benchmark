
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 39 elements
    if len(my_list) < 39:
        return False

    # Get the integer at index 38
    num = my_list[38]

    # Check if the integer is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i + num / i

            if sum == num:
                return True

    return False
