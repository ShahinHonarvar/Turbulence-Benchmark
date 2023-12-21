
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 90 and 41
    num1 = my_list[90]
    num2 = my_list[41]
    if num1 > num2:
        smaller_num = num2

    else:

        smaller_num = num1


    for i in range(2, smaller_num + 1):

        if num1 % i == 0 and num2 % i == 0:

            gcf = i


            break


    return gcf
