
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers until
    # they are equal or one is zero.
    num1 = my_list[360]
    num2 = my_list[722]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2

        else:
            num2 -= num1

    return num1
