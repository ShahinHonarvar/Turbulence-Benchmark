
def if_perfect_num(my_list):
    if len(my_list) < 27:
        return False

    num = my_list[27]
    sum = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    return sum == num
