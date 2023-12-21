
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers at indices 24 and 68
    num1 = my_list[24]
    num2 = my_list[68]
    if num1 > num2:
        smaller_num = num2

    else:

        smaller_num = num1


    for i in range(2, int(smaller_num ** 0.5) + 1):

        if num1 % i == 0 and num2 % i == 0:

            gcf = i


            break


    return gcf
