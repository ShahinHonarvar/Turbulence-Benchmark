
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two integers at indices 54 and 13 in the list
    num1 = my_list[54]
    num2 = my_list[13]
    if num1 > num2:
        small_num = num2
        large_num = num1

    else:

        small_num = num1

        large_num = num2

    for i in range(1, small_num + 1):

        if large_num % i == 0 and small_num % i == 0:

            common_factor = i

            break

    return common_factor
