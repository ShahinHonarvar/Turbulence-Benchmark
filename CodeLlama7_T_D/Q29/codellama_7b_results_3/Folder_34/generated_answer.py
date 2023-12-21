
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers at indices 60 and 64
    num1 = my_list[60]
    num2 = my_list[64]
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
