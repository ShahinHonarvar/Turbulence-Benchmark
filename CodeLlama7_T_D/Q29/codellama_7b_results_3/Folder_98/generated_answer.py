
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers until their
    # remainder is 0 or 1.
    num1 = my_list[0]
    num2 = my_list[9]
    while True:
        if (num1 % 2 == 0) and (num2 % 2 == 0):
            num1 /= 2
            num2 /= 2
        else:
            break

    return num1
