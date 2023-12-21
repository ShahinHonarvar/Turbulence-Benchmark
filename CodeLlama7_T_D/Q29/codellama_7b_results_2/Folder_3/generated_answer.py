
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple until they are equal

    num1 = my_list[47]
    num2 = my_list[10]

    if num1 > num2:
        num1, num2 = num2, num1

    while num1 != num2:
        if num1 % 2 == 0 and num2 % 2 == 0:
            num1 //= 2
            num2 //= 2

        else:
            num1 -= 1
            num2 += 1

    return num1
