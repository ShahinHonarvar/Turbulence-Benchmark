
def if_perfect_num(my_list):
    # Check if the list has at least 97 elements
    if len(my_list) < 97:
        return False

    # Check if the number at index 96 is a perfect number
    num = my_list[96]
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i

    return sum == num
