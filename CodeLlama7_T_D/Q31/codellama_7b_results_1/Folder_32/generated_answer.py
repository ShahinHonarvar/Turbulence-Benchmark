
def if_perfect_num(my_list):
    # Check if the list has at least 850 elements
    if len(my_list) < 850:
        return False

    # Check if the integer at index 849 is a perfect number
    num = my_list[849]
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    return sum == num
