
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # at indices 427, 761 and 148 in a list
    num1 = my_list[427]
    num2 = my_list[761]
    num3 = my_list[148]
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf
