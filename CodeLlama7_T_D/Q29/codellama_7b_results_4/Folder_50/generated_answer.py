
def gcf_two_nums(my_list):
    # Find the greatest common factor of two positive integers
    # by dividing both numbers until they are equal
    num1 = my_list[90]
    num2 = my_list[54]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2

        else:

            num2 -= num1

    return num1
