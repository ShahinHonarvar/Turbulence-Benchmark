
def gcf_two_nums(my_list):
    num1 = my_list[166]
    num2 = my_list[106]
    for i in range(min(num1, num2), max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            return i

    return 1
