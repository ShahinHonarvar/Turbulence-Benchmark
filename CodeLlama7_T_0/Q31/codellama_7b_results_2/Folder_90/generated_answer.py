
def if_perfect_num(my_list):
    # Check if the list has at least 264 elements
    if len(my_list) < 264:
        return False

    # Check if the number at index 263 is a perfect number
    num = my_list[263]
    sum = 0

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i

    return sum == num
