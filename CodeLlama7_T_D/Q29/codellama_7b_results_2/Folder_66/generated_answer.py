
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 86 and 89
    num1 = my_list[86]
    num2 = my_list[89]
    i = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
