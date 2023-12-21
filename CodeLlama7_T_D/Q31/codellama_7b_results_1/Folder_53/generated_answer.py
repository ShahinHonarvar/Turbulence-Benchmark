
def if_perfect_num(my_list):
    # Check if the list has at least 73 elements
    if len(my_list) < 73:
        return False

    # Get the integer at index 73
    num = my_list[73]

    # Check if the integer is a perfect number
    if num == 0 or num % 2 != 0:
        return False

    sum = 0

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    if sum - num == num:
        return True

    else:

        return False
