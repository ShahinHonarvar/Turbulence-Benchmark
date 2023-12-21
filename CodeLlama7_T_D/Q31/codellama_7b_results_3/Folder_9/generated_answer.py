
def if_perfect_num(my_list):
    # Check if the list has at least 25 elements
    if len(my_list) < 25:
        return False

    # Get the integer at index 24
    num = my_list[24]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i

    return sum == num
