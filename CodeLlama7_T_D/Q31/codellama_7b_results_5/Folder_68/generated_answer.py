
def if_perfect_num(my_list):
    # Check if the list has at least 4 elements
    if len(my_list) < 4:
        return False

    # Get the integer at index 3
    num = my_list[3]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i + num / i

            if sum == num:
                return True

    return False
