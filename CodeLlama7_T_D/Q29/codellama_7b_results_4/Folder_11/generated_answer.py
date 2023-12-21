
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 64 and 80
    num1 = my_list[64]
    num2 = my_list[80]
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    return num1
