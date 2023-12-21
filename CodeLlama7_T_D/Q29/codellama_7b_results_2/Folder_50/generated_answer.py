
def gcf_two_nums(my_list):
    num1 = my_list[90]
    num2 = my_list[54]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            return i

    return 1
