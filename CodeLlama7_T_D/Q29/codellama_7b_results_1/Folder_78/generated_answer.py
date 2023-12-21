
def gcf_two_nums(my_list):
    num1 = my_list[54]
    num2 = my_list[13]
    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:

        smaller_num = num1

        larger_num = num2

    for i in range(1, min(smaller_num, larger_num) + 1):

        if smaller_num % i == 0 and larger_num % i == 0:

            common_factor = i

    return common_factor
