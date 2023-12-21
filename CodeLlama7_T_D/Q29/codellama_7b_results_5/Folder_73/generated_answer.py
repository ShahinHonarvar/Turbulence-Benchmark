
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their remainder
    # until they have no remainders

    num1 = my_list[51]
    num2 = my_list[27]
    while num1 % 2 == 0 and num2 % 2 == 0:
        num1 //= 2
        num2 //= 2
    if num1 > num2:
        return num1
    else:
        return num2
