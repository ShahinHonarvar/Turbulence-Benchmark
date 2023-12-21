
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 85, 36 and 54
    num1 = my_list[85]
    num2 = my_list[36]
    num3 = my_list[54]
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if (num1 % i == 0) and (num2 % i == 0) and (num3 % i == 0):
            gcf = i

    return gcf
