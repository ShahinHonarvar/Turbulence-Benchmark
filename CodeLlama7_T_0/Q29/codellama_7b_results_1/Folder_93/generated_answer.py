
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 78 and 16
    num1 = my_list[78]
    num2 = my_list[16]
    if num1 > num2:
        smaller_num = num2

    else:

        smaller_num = num1


    for i in range(1, smaller_num + 1):

        if num1 % i == 0 and num2 % i == 0:

            gcf = i


    return gcf
